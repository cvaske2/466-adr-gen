from tkinter import *
from tkinter import ttk
from  peer_to_peer_adr import *
from layered_adr import *

def open_peer_to_peer_style():
    root = Tk()
    peer_to_peer_frame(root)

def open_layered_style():
    root = Tk()
    layered_frame(root)

root = Tk()
frame = ttk.Frame(root, padding=10)
frame.grid()

ttk.Label(frame, text="Hello").grid(column=0, row=0)
ttk.Button(frame, text="Peer to Peer Style frame", command=open_peer_to_peer_style).grid(column=0, row=1)
ttk.Button(frame, text="Layered Style frame", command=open_layered_style).grid(column=0, row=2)


root.mainloop()
