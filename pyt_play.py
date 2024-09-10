from pytube import YouTube
import os
from moviepy.editor import *

def yt_dl(link, dir):
    yt = YouTube(link)
    yt.streams.filter(only_audio=True, file_extension="mp4").first().download(output_path=dir)
    return yt.streams.filter(only_audio=True, file_extension="mp4").first().default_filename

def mp4_to_mp3(filein, fileout):
    if not os.path.exists(fileout):
        audio = AudioFileClip(filein)
        audio.write_audiofile(fileout, logger=None)
