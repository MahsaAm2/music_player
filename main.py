import tkinter.messagebox
from tkinter import *
from pygame import mixer
from tkinter import filedialog
import tkinter.messagebox

window = Tk()
mixer.init()


def play_music():
   try:
       paused

   except:
       try:
           mixer.music.load(filename)
           mixer.music.play()
           statusbar['text'] = "Music is playing"
       except:
           tkinter.messagebox.showerror("Error", "File not found")
   else:
       mixer.music.unpause()
       statusbar['text'] = "Music is playing"


def stop_music():
    mixer.music.stop()
    statusbar['text'] = "Music is stopped"


def pause_music():
    global paused
    paused = True
    mixer.music.pause()
    statusbar['text'] = "Music is paused"


def rewind_music():
    play_music()
    statusbar['text'] = "Music is rewinded"



def set_volume(value):
    vol = int(value)/100
    mixer.music.set_volume(vol)


def browse_file():
    global filename
    filename = filedialog.askopenfilename()


def help_me():
    tkinter.messagebox.showinfo("Help", "How can I help you? ")


window.geometry('800x300')
window.title('Music Player')

menubar = Menu(window)
submenu = Menu(menubar, tearoff=0)

window.config(menu=menubar)
menubar.add_cascade(label="File", menu=submenu)

submenu.add_command(label="Open", command=browse_file)
submenu.add_command(label="Exit", command=window.destroy)


submenu2 = Menu(menubar, tearoff=0)
submenu2.add_command(label="Help", command=help_me)
menubar.add_cascade(label="About Us", menu=submenu2)

textLabel = Label(window, text="Music Player", font=("Arial", 20), foreground="#007273")
textLabel.pack()

frame = Frame(window)
frame.pack(padx=10, pady=10)

photo = PhotoImage(file='play0.png')
playButton = Button(frame, image=photo, command=play_music, borderwidth=0)
playButton.grid(row=0, column=0, padx=10)

photo1 = PhotoImage(file='icons8-stop-100.png')
stopButton = Button(frame, image=photo1, command=stop_music, borderwidth=0)
stopButton.grid(row=0, column=1, padx=10)

photo2= PhotoImage(file='pause.png')
pauseButton = Button(frame, image=photo2, command=pause_music, borderwidth=0)
pauseButton.grid(row=0, column=2, padx=10)

bottomframe = Frame(window)
bottomframe.pack()
rewindphoto = PhotoImage(file='icons8-repeat-100.png')
rewBtn = Button(bottomframe, image=rewindphoto, command=rewind_music, borderwidth=0)
rewBtn.grid(row=0, column=0)

scale = Scale(bottomframe, from_=0, to=100, orient=HORIZONTAL, command=set_volume, foreground="#007273")
scale.set(70)
scale.grid(row=0, column=1)

statusbar = Label(window, text="Keep enjoying the music", relief=SUNKEN, anchor=W, font=("Arial", 12), foreground="#007273")
statusbar.pack(side=BOTTOM, fill=X)


window.mainloop()