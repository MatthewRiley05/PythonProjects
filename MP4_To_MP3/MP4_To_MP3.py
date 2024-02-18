import moviepy.editor
import sys
import os

droppedFile = sys.argv[1]

# Get the filename without extension
base = os.path.basename(droppedFile)
filename_without_extension = os.path.splitext(base)[0]

mp3_file = filename_without_extension + ".mp3"

video = moviepy.editor.VideoFileClip(droppedFile)
audio = video.audio

audio.write_audiofile(mp3_file)