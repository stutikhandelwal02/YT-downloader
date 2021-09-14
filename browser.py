from tkinter import *
from tkinter import  messagebox
import pytube
from pytube import YouTube
from tkinter import ttk
import tkinter.filedialog as filedialog

root = Tk()
root.geometry("600x400")
root.title("YT Downloader")
root.config(bg="pink")

url=""

def browse_path():
    foldername = filedialog.askdirectory()
    file_path.insert(END, foldername)


def down_load():
    global url
    url = e.get()
    yt = pytube.YouTube(url)
    file = file_path.get()
    if var.get()==1:
        video = yt.streams.get_by_resolution('144p')
    elif var.get()==2:
        video = yt.streams.get_by_resolution('360p')
    elif var.get() == 3:
        video = yt.streams.get_by_resolution('720p')
    elif var.get() == 4:
        video = yt.streams.get_by_resolution('1080p')

    try:
        video.download(file)
    except AttributeError:
        messagebox.showerror(title="Not Found",message="Video quality not available please try another one")


f1=Frame(root)
f1.pack()

l1=Label(f1,text="YouTube Downloader",font="large 20",bg="pink")
l1.pack()

l2=Label(text="Enter Url :",font='medium 15',bg="pink")
l2.pack(pady=10)

e=ttk.Entry(root,font="medium 15",width=30)
e.pack(pady=0)

l3 = Label(text="Enter path...",font="medium 15",bg="pink")
l3.pack(pady=15)

file_path=ttk.Entry(root,font="medium 15",width=30)
file_path.pack(pady=0)

b1 = Button(root,text="Browse",font="10",command=browse_path)
b1.place(x=480,y=165)
var = IntVar()
values = [
    ("144p"),
    ("360p"),
    ("720p"),
    ("1080p")
]

for v in range(0,4):
    rb = ttk.Radiobutton(root,
                         text=values[v],
                         value=v+1,
                         variable=var)
    rb.place(x=150+(v*80),y=230)

b1=ttk.Button(root,text="Download",width=20,command=down_load)
b1.pack(pady=70)

root.mainloop()