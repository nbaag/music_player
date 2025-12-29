import os
from tkinter import filedialog
from tkinter import *
import vlc

root = Tk()
root.title("music_player")
root.geometry("700x500")

# Create Frames in root window
info_frame = Frame(root)
info_frame.pack(fill="both", expand=True, padx="5", pady="5")
control_frame = Frame(root)
control_frame.pack(side="bottom")

#Create song list in info_frame
songlist = Listbox(info_frame, bg="black", fg="white", width="50")
songlist.pack(padx="5", pady="5", expand=True, side="left", fill="both")

# Create track info in info_frame
track_label = Label(info_frame, text="Информация о треке", bg="lightgray", font=("Arial", 12, "bold"))
track_label.pack(pady=10)

# Add info about song

# Add images
play_btn_image = PhotoImage(file='icons/play32.png')
pause_btn_image = PhotoImage(file='icons/pause32.png')
next_btn_image = PhotoImage(file='icons/next32.png')
previous_btn_image = PhotoImage(file='icons/previous32.png')

# Create control_frame for buttons
control_frame = Frame(root)
control_frame.pack(side="bottom")

# Add buttons to control_frame
play_btn = Button(control_frame, image=play_btn_image, borderwidth=1).grid(row=0, column=0, padx=7, pady=10)
pause_btn = Button(control_frame, image=pause_btn_image, borderwidth=1).grid(row=0, column=1, padx=7, pady=10)
previous_btn = Button(control_frame, image=previous_btn_image, borderwidth=1).grid(row=0, column=2, padx=7, pady=10)
next_btn = Button(control_frame, image=next_btn_image, borderwidth=1).grid(row=0, column=3, padx=7, pady=10)



root.mainloop()