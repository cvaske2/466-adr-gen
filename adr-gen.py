from tkinter import *
from tkinter import ttk

root = Tk()
frame = ttk.Frame(root, padding=10)
frame.grid()

ttk.Label(frame, text="Hello").grid(column=0, row=0)
ttk.Button(frame, text="Exit", command=root.destroy).grid(column=0, row=1)

root.mainloop()