import sys
from tkinter import *
from tkinter import ttk

# Grab args and slice off first (name of executable)
ARGS = sys.argv[1:]


if len(ARGS) != 0 and ARGS[0] in ['help', '-help', '--help', '-h', '--h']:
    print("Here are some parameters available to you:") # TODO: implement
    print()
    exit()

root = Tk()
frame = ttk.Frame(root, padding=10)
frame.grid()


ttk.Label(frame, text="Hello").grid(column=0, row=0)
ttk.Button(frame, text="Exit", command=root.destroy).grid(column=0, row=1)

root.mainloop()