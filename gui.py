"""
from tkinter import *
#creating the application main window.
top = Tk()
Entry
#Entering the event main loop
top.mainloop()
"""
import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
canvas = tk.Canvas(root , height=500, width=500, bg="SkyBlue3")
canvas.pack()
frame = tk.Frame(root , bg = "gray77")
frame.place(relwidth=0.8, relheight=0.6, relx=0.1, rely=0.1)
openfile=tk.Button(root, text = "Open App", padx=10, pady=5, fg="gray4", bg="white", command=openApp)
openfile.pack()
runapps=tk.Button(root, text = "Run App", padx=10, pady=5, fg="gray4", bg="white")
runapps.pack()
root.mainloop()