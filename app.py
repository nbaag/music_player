from tkinter import *
import pygame
import os

root = Tk()
root.title("music_player")
root.geometry("700x500")

pygame.mixer.init()

songlist = Listbox(root, bg="black", fg="white", width="50")
songlist.pack(pady="5", padx="5", side="left", fill="both")

play_btn_image = PhotoImage(file='icons/play32.png')
pause_btn_image = PhotoImage(file='icons/pause32.png')
next_btn_image = PhotoImage(file='icons/next32.png')
previous_btn_image = PhotoImage(file='icons/previous32.png')

control_frame = Frame(root)
control_frame.pack()

play_btn = Button(control_frame, image=play_btn_image, borderwidth=1).grid(row=0, column=0, padx=7, pady=10)
pause_btn = Button(control_frame, image=pause_btn_image, borderwidth=1).grid(row=0, column=1, padx=7, pady=10)
previous_btn = Button(control_frame, image=previous_btn_image, borderwidth=1).grid(row=0, column=2, padx=7, pady=10)
next_btn = Button(control_frame, image=next_btn_image, borderwidth=1).grid(row=0, column=3, padx=7, pady=10)

root.mainloop()