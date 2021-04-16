# pip install
# pytube 
# PySimpleGUI
# moviepy
import pytube, glob
import PySimpleGUI as sg
from moviepy.editor import *

files = glob.glob("temp/*")
for f in files:
    os.remove(f)

if not os.path.exists('music'):
    os.mkdir('music')

if not os.path.exists('video'):
    os.mkdir('video')

if not os.path.exists('temp'):
    os.mkdir('temp')

sg.theme('DarkTeal4')

layout = [
    [sg.Text('YouTube Link', size=(11, 1)), sg.InputText('', size=(23, 1))],
    [sg.Text('Resolution', size=(11, 1)), sg.InputText('', size=(23, 1))],
    [sg.Text('File Type', size=(11, 1)), sg.Radio('mp4', "RADIO1"), sg.Radio('mp3', "RADIO1")],
    [sg.Submit(button_text='Download')]
]

window = sg.Window('YouTube Downloader', layout)

def dl():
    yt = pytube.YouTube(link)
    print("Video Found")
    print("Downloading...")
    if mp3:
        ys = yt.streams.filter(only_audio=True)
        ys = yt.streams.first()
        title = yt.title
        ys.download(r"temp/")
        while True:
            if glob.glob("temp/" + title + ".mp4"):
                print("Downloaded")
                print("Converting from mp4 to mp3...")
                video = VideoFileClip(os.path.join("temp/" + title + ".mp4"))
                video.audio.write_audiofile(os.path.join("music/" + title + ".mp3"))
                video.close()
                print("Done")
                break
    else:
        ys = yt.streams.filter(file_extension="mp4", res=res)
        ys = yt.streams.first()
        ys.download(r"video/")
        print("Downloaded")

while True:
    event, values = window.read()

    if event is None:
        print('exit')
        break

    if event == "Download":
        link = values[0]
        res = int(values[1])
        if values[2]:
            mp3 = False
        else:
            mp3 = True
        dl()

window.close()
