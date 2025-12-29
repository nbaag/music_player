import os
from tkinter import filedialog
from tkinter import *
import vlc
from mutagen import File


root = Tk()
root.title("music_player")
root.geometry("700x500")

menubar = Menu(root)
root.config(menu=menubar)

songs = []
current_song = ""
paused = False

def load_music():
    global current_song, songs

    songs.clear()
    songlist.delete(0, END)

    root.directory = filedialog.askdirectory()
    if not root.directory:
        return

    for filename in os.listdir(root.directory):
        name, ext = os.path.splitext(filename)
        if ext.lower() == ".flac":
            full_path = os.path.join(root.directory, filename)

            title, artist = get_track_info(full_path)

            songs.append({
                "path": full_path,
                "title": title,
                "artist": artist
            })

            songlist.insert(END, f"{artist} — {title}")

    if songs:
        songlist.select_set(0)
        current_song = songs[0]["path"]


def get_track_info(filepath):
    audio = File(filepath, easy=True)

    if audio is None:
        return "Unknown", "Unknown"
    
    title = audio.get("title", ["Unknown title"])[0]
    artist = audio.get("artist", ["Unknown artist"])[0]

    return title, artist

organise_menu = Menu(menubar, tearoff=False)
organise_menu.add_command(label='Select Folder', command=load_music)
menubar.add_cascade(label='Organise', menu=organise_menu)

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