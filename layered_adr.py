from tkinter import ttk

    
def layered_frame(parent):
    new_frame = ttk.Frame(parent, padding=10)
    new_frame.grid()
    ttk.Label(new_frame, text="This is a Layered style frame!").grid(column=0, row=0)
    # Create a label and add it to the frame
    ttk.Label(new_frame, text="Status:").grid(column=0, row=2)

    # Create an entry widget and add it to the frame
    status_entry = ttk.Entry(new_frame)
    status_entry.grid(column=0, row=3)

    # Create another label and add it to the frame
    ttk.Label(new_frame, text="Context:").grid(column=0, row=5)

    # Create another entry widget and add it to the frame
    context_entry = ttk.Entry(new_frame)
    context_entry.grid(column=0, row=6)

    # Create a label and add it to the frame
    ttk.Label(new_frame, text="Decision:").grid(column=0, row=8)

    ttk.Label(new_frame, text="Layering:").grid(column = 0, row=9)
    
    layering_entry = ttk.Entry(new_frame)
    layering_entry.grid(column=1, row=10)

    ttk.Label(new_frame, text="Communication:").grid(column = 0, row=11)
    
    communication_entry = ttk.Entry(new_frame)
    communication_entry.grid(column=1, row=12)

    ttk.Label(new_frame, text="Interfaces:").grid(column = 0, row=13)
    
    interfaces_entry = ttk.Entry(new_frame)
    interfaces_entry.grid(column=1, row=14)


    ttk.Label(new_frame, text="Rationale:").grid(column=0, row=16)
    rationale_entry = ttk.Entry(new_frame)
    rationale_entry.grid(column=0, row=17)

    ttk.Button(new_frame, text="Close", command=new_frame.destroy).grid(column=0, row=19)
