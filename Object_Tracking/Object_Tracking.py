import cv2

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

tracker = cv2.TrackerCSRT_create()
success, img = video.read()
bbox = cv2.selectROI("Tracking", img, False)
tracker.init(img, bbox)

def drawBox():
    global bbox
    x, y, w, h = [int(i) for i in bbox]
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 255), 2, 1)
    cv2.putText(img, "Tracking", (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (46, 125, 50), 2)

while True:
    timer = cv2.getTickCount()
    success, img = video.read()
    
    success, bbox = tracker.update(img)
    
    if success:
        drawBox()
    else:
        cv2.putText(img, "Lost", (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    
    fps = round(cv2.getTickFrequency() / (cv2.getTickCount() - timer), 2)
    cv2.putText(img, "FPS: " + str(fps), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (46, 125, 50), 2)
    cv2.imshow("Tracking", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break