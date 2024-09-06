from pytube import YouTube
from playsound import playsound

def yt_dl(link):
    yt = YouTube(link)
    yt.streams.filter(only_audio=True).get_by_itag(249).download()
    print(yt.streams.filter(only_audio=True))

#yt_dl('https://www.youtube.com/watch?v=p-Z3YrHJ1sU')

playsound('C:/Users/awajnsztejn/OneDrive - Rehabilitation Centre for Children, Inc/Documents/Py/PyT/StereoLove.mp3')