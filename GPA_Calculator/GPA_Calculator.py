import art
letterGrade = {"A+" : 4.3,
               "A" : 4.0,
               "A-" : 3.7,
               "B+" : 3.3,
               "B" : 3.0,
               "B-" : 2.7,
               "C+" : 2.3,
               "C" : 2.0,
               "C+" : 1.7,
               "D+" : 1.3,
               "D" : 1.0,
               "F" : 0}
credits = []
grade = []   
courseCount = int(input("Please enter the total number of courses taken: "))

for i in range(courseCount):
    creditInput = int(input('\nPlease enter the credit value for course number {}: '.format(i+1)))
    credits.append(creditInput)
    gradeInput = input('\nPlease enter the letter grade received for course number {}: '.format(i+1))
    grade.append(gradeInput)
    
def gpaCalculate():
    total = 0
    for i in range(courseCount):
        total += (credits[i-1] * letterGrade[grade[i-1]]) 
    finalGPA = int(total/sum(credits))
    gpaArt = art.text2art(str(finalGPA))
    print("\n" + gpaArt)
    if 0 <= finalGPA < 3:
        print("Kill yourself you dumbfuck\n")
    elif 3 <= finalGPA <= 3.5:
        print("Okay na yan but could be better\n")
    elif 3.5 < finalGPA < 4.0:
        print("Holy shit das crazy\n")
    else:
        print("I KNEEL\n")

gpaCalculate()
input("Press any key to leave the program...")