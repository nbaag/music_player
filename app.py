from tkinter import filedialog
from tkinter import *
import pygame
import os

root = Tk()
root.title("music_player")
root.geometry("700x500")

pygame.mixer.init()

menubar = Menu(root)
root.config(menu=menubar)

songs = []
current_song = ""
paused = False

def load_music():
    global current_song
    root.directory = filedialog.askdirectory()

    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext == '.flac':
            songs.append(song)

    for song in songs:
        songlist.insert("end", song)

    songlist.selection_set(0)
    current_song = songs[songlist.curselection()[0]]

def play_music():
    global current_song, paused

    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory, current_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused = False

def pause_music():
    global paused

    pygame.mixer.music.pause()
    paused = True

def next_music():
    global current_song, paused
    try:
        songlist.select_clear(0, END)
        songlist.select_set(songs.index(current_song) + 1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass

def prev_music():
    global current_song, paused

    try:
        songlist.select_clear(0, END)
        songlist.select_set(songs.index(current_song) - 1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass

organise_menu = Menu(menubar, tearoff=False)
organise_menu.add_command(label='Select Folder', command=load_music)
menubar.add_cascade(label='Organise', menu=organise_menu)

songlist = Listbox(root, bg="black", fg="white", width="50")
songlist.pack(pady="5", padx="5", fill="both", expand=True)

play_btn_image = PhotoImage(file='icons/play32.png')
pause_btn_image = PhotoImage(file='icons/pause32.png')
next_btn_image = PhotoImage(file='icons/next32.png')
previous_btn_image = PhotoImage(file='icons/previous32.png')

control_frame = Frame(root)
control_frame.pack(side="bottom")

play_btn = Button(control_frame, image=play_btn_image, borderwidth=1, command=play_music).grid(row=0, column=0, padx=7, pady=10)
pause_btn = Button(control_frame, image=pause_btn_image, borderwidth=1, command=pause_music).grid(row=0, column=1, padx=7, pady=10)
previous_btn = Button(control_frame, image=previous_btn_image, borderwidth=1, command=prev_music).grid(row=0, column=2, padx=7, pady=10)
next_btn = Button(control_frame, image=next_btn_image, borderwidth=1, command=next_music).grid(row=0, column=3, padx=7, pady=10)

root.mainloop()