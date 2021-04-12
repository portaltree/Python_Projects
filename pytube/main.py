import pytube
import tkinter as tk
from moviepy.editor import *
import glob

if not os.path.exists('music'):
    os.mkdir('music')

if not os.path.exists('video'):
    os.mkdir('video')

win = tk.Tk()
win.title("Youtube Video Downloader")
win.geometry("400x300")

label = tk.Label(win, text="URL")
label.pack()

text = tk.Entry(win)
text.pack()
text.insert(tk.END, "")

OptionList = [
"1080",
"720",
"480",
"360",
"240",
"144"
]

label2 = tk.Label(win, text="Resolution")
label2.pack()

variable = tk.StringVar(win)
variable.set(OptionList[0])

opt = tk.OptionMenu(win, variable, *OptionList)
opt.pack()

label3 = tk.Label(win, text="Format")
label3.pack()

var = tk.IntVar()
var.set(0)

rdo1 = tk.Radiobutton(win, value=0, variable=var, text='mp3')
rdo1.place(x=150, y=110)

rdo2 = tk.Radiobutton(win, value=1, variable=var, text='mp4')
rdo2.place(x=200, y=110)

def dl():
    if var.get() == 0:
        mp3 = True
        print("Finding Video...")
    else:
        mp3 = False
        print("Finding Video...")
    link = text.get()
    res = int(variable.get())
    yt = pytube.YouTube(link)
    print("Video Found")
    print("Downloading...")
    if mp3:
        ys = yt.streams.filter(only_audio = True)
        ys = yt.streams.first()
        title = yt.title
        ys.download(r"music/")
        print("Downloaded")
        print("Converting from mp4 to mp3...")
        video = VideoFileClip(os.path.join("music/" + title + ".mp4"))
        video.audio.write_audiofile(os.path.join("music/" + title + ".mp3"))
        while glob.glob("music/" + title + ".mp4"):
            if glob.glob("music/" + title + ".mp3"):
                video.reader.close()
                if video.audio and video.audio.reader:
                    video.audio.reader.close_proc()
                os.remove("music/" + title + ".mp4")
                print("Done")
    else:
        ys = yt.streams.filter(file_extension = "mp4", res = res)
        ys = yt.streams.first()
        ys.download(r"video/")
        print("Downloaded")

okButton = tk.Button(win, text="Download", command=dl)
okButton.place(x=165, y=135)

win.mainloop()
