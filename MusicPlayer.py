import sys
import os
from tkinter import *
from tkinter import filedialog
from pygame import mixer
import time
from mutagen.mp3 import MP3 # this module will scan the mp3 songs and display the total time of the song
import tkinter.ttk as ttk





# GRAB SONG LENGTH TIME

def playTime():
    # get current song elapsed time
    current_time = int(mixer.music.get_pos()/1000)  # gets the current position in seconds
                                                    # converted to integer
    #convert to time format
    converted_current_time = time.strftime('%M:%S', time.gmtime(current_time)) # this converts the normal time of current_time into Hours, minutes and seconds


    # Get the currently playing song
    current_song = my_lisbox.curselection() # returns a number
    
    # now to convert this number into actual song title
    song = my_lisbox.get(current_song) # will give the song title from the listbox

    # add directory structure and mp3 to song tile
    song_ = f'E:/Audio/{song}'

    # now to look it up in mutagen
    global song_mut

    song_mut = MP3(song_) #passing the song that we want to look up

    #get song length
    #global song_length
    song_length = song_mut.info.length

    # now to convert into time format
    converted_song_length = time.strftime('%M:%S', time.gmtime(song_length))


    # Output time to status bar
    status.config(text=f'Time Elapsed: {converted_current_time} of {converted_song_length}')
    
    # We need to update the time
    # Since the songs keeps playing, the time must update itself too

    status.after(1000, playTime)    # This updates the label
                                    # every 1000 miliseconds, so every 1 second,
                                    # after every 1000 miliseconds it calls the playTime() function
def openSong():
    # open file dialog
    song = filedialog.askopenfilename(initialdir='E:/Audio', title='Select a song', filetypes=(('Mp3 files', '*.mp3'),('All files', '*.*') ))
    song = song.replace("E:/Audio/", "")
    my_lisbox.insert(END, song)
    
def delAll():
    my_lisbox.delete(0, END)

def selectFile():
    x = my_lisbox.get(ANCHOR)
    mixer.music.load('E:/Audio/'+x)
    mixer.music.set_volume(0.7)
    mixer.music.play()
    
    # Call the playTime function to get song length
    playTime()
 

def toggleSong():
    mixer.music.pause()

def stopMusic():
    mixer.music.stop()
    # Clear the status
    status.config(text='')

def delsong():
    my_lisbox.delete(ANCHOR)

def resume():
    mixer.music.unpause()

   




root = Tk()
root.title('tkinter Music Player')
root.iconbitmap('D:/Icons/star.ico')
root.geometry('600x450')
#root.configure(background='grey')

mixer.init()

# initializing the menu
my_menu = Menu(root)
root.config(menu=my_menu)

# creating the menu item

file_menu = Menu(my_menu) # defining
my_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Add Song', command=openSong)
file_menu.add_separator() # will have a separator line
file_menu.add_command(label='Delete Song', command=delsong)

file_menu.add_command(label='Delete All', command=delAll)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.quit)


# scrollbar
#my_scrollbar = Scrollbar(my_frame, orient=VERTICAL) # vertical orientation of scrollbar

# listbox
my_lisbox = Listbox(root, width=90, height=12, borderwidth=3, fg='green', bg='black')#,yscrollcommand=my_scrollbar.set)

# creating a frame
my_frame = Frame(root)

my_lisbox.pack(pady=20)
#my_frame.pack()
my_button = Button(my_frame, text='Play Song', padx=20, pady=10, bg='green', fg='white', font='Times 12 bold', command=selectFile)
second_button = Button(my_frame, text='Pause', padx=17, pady=10, bg='blue', fg='white', font='Times 12 bold', command=toggleSong)
stop_button = Button(my_frame, text='Stop', padx=20, pady=10, bg='red', fg='white', font='Times 12 bold', command=stopMusic)
resume_button = Button(my_frame, text='Unpause', padx=20, pady=10, bg='blue', fg='white', font='Times 12 bold', command=resume)
stop_button.grid(row=0, column=0, padx=10)

my_button.grid(row=0, column=1, padx=12)
second_button.grid(row=0, column=2, padx=10)
resume_button.grid(row=0, column=3, padx=12)
my_frame.pack()

# Adding song length
status = Label(root, text='', bd=1, relief=GROOVE, anchor=E) #achor=E will anchor the label to the right
status.pack(fill=X, side=BOTTOM, ipady=2) #fill=X will fill it across the screen

#creating a temporary slider label
slider_label = Label(root, text='0')
slider_label.pack()

root.mainloop()