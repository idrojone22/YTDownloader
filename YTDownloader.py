import os
import pytube

path = "/home/jordi/.local/bin"
os.environ["PATH"] += os.pathsep + path

link = input('Enter YouTube Video URL: ')
yt = pytube.YouTube(link)

try:
    video = yt.streams.first()
    video.download('./')
    print('Successfully downloaded video:' +  link)
except Exception as e:
    print(f'Error while downloading video: {e}')

