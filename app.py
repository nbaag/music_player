from tkinter import *
import pygame
import os

root = Tk()
root.title("music_player")
root.geometry("700x500")
root.grid()

pygame.mixer.init()

songlist = Listbox(root, bg="black", fg="white", width="50")
songlist.pack(pady="5", padx="5", side="left", fill="both")

root.mainloop()