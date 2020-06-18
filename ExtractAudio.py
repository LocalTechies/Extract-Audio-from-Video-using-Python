#install moviepy
#CMD/Pycharm ---> pip install moviepy
#Anaconda ---> conda install moviepy

#import editor class in moviepy module
import moviepy.editor

#import video for which audio to be extracted
video = moviepy.editor.VideoFileClip("video.mp4")

#Extracting Audio from video
audio = video.audio

#saving the extracted audio file
audio.write_audiofile("audio.mp3")
