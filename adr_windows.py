import sys
from tkinter import *
from tkinter import ttk


def open_cs():
    '''
    Opens a window and adds content based on the data read from the template.
    Parameter: None
    Returns: Saved copy of the template
    '''
    def save_input():
        with open("client_server_style_adr.md", "w") as f:
            f.write(f"Status: {status_text.get(1.0, END)}")
            f.write(f"Context: {context_text.get(1.0, END)}")
            f.write(f"Decision:\n")
            f.write(f"  Client: {client_text.get(1.0, END)}")
            f.write(f"  Server: {server_text.get(1.0, END)}")
            f.write(f"Communication: {communication_text.get(1.0, END)}")
            f.write(f"Interfaces: {interfaces_text.get(1.0, END)}")
            f.write(f"Rationale: {rationale_text.get(1.0, END)}")
            f.write(f"Consequences: {consequences_text.get(1.0, END)}")
            f.write(f"References: {references_text.get(1.0, END)}")


    subroot = Tk()
    subroot.title("Client-Server Style ADR")

    # Create labels and text boxes for each section of the template
    ttk.Label(subroot, text="Status: ").grid(column=0, row=0, sticky="W")
    status_text = Text(subroot, height=2, width=60)
    status_text.grid(column=1, row=0)

    ttk.Label(subroot, text="Context: ").grid(column=0, row=1, sticky="W")
    context_text = Text(subroot, height=5, width=60)
    context_text.grid(column=1, row=1)

    ttk.Label(subroot, text="Decision: ").grid(column=0, row=2, sticky="W")
    decision_frame = ttk.Frame(subroot, padding=10)
    decision_frame.grid(column=1, row=2)

    ttk.Label(decision_frame, text="Client: ").grid(column=0, row=0, sticky="W")
    client_text = Text(decision_frame, height=5, width=60)
    client_text.grid(column=1, row=0)

    ttk.Label(decision_frame, text="Server: ").grid(column=0, row=1, sticky="W")
    server_text = Text(decision_frame, height=5, width=60)
    server_text.grid(column=1, row=1)

    ttk.Label(subroot, text="Communication: ").grid(column=0, row=3, sticky="W")
    communication_text = Text(subroot, height=5, width=60)
    communication_text.grid(column=1, row=3)

    ttk.Label(subroot, text="Interfaces: ").grid(column=0, row=4, sticky="W")
    interfaces_text = Text(subroot, height=5, width=60)
    interfaces_text.grid(column=1, row=4)

    ttk.Label(subroot, text="Rationale: ").grid(column=0, row=5, sticky="W")
    rationale_text = Text(subroot, height=5, width=60)
    rationale_text.grid(column=1, row=5)

    ttk.Label(subroot, text="Consequences: ").grid(column=0, row=6, sticky="W")
    consequences_text = Text(subroot, height=5, width=60)
    consequences_text.grid(column=1, row=6)

    ttk.Label(subroot, text="References: ").grid(column=0, row=7, sticky="W")
    references_text = Text(subroot, height=2, width=60)
    references_text.grid(column=1, row=7)

    save_button = ttk.Button(subroot, text="Save", command=save_input)
    save_button.grid(column=1, row=8)




def open_data_flow_template():
    def save_input():
        with open("data_flow_style_adr.md", "w") as f:
            f.write(f"Status: {status_text.get(1.0, END)}")
            f.write(f"Context: {context_text.get(1.0, END)}")
            f.write(f"Decision:\n")
            f.write(f"  Data sources: {data_sources_text.get(1.0, END)}")
            f.write(f"  Data sinks: {data_sinks_text.get(1.0, END)}")
            f.write(f"  Processing: {processing_text.get(1.0, END)}")
            f.write(f"  Communication: {communication_text.get(1.0, END)}")
            f.write(f"  Interfaces: {interfaces_text.get(1.0, END)}")
            f.write(f"Rationale: {rationale_text.get(1.0, END)}")
            f.write(f"Consequences: {consequences_text.get(1.0, END)}")
            f.write(f"References: {references_text.get(1.0, END)}")

    subroot = tk.Tk()
    subroot.title("Data-Flow Style ADR")

    # Create labels and text boxes for each section of the template
    ttk.Label(subroot, text="Status: ").grid(column=0, row=0, sticky="W")
    status_text = Text(subroot, height=2, width=60)
    status_text.grid(column=1, row=0)

    ttk.Label(subroot, text="Context: ").grid(column=0, row=1, sticky="W")
    context_text = Text(subroot, height=5, width=60)
    context_text.grid(column=1, row=1)

    ttk.Label(subroot, text="Decision: ").grid(column=0, row=2, sticky="W")
    decision_frame = ttk.Frame(subroot, padding=10)
    decision_frame.grid(column=1, row=2)

    ttk.Label(decision_frame, text="Data sources: ").grid(column=0, row=0, sticky="W")
    data_sources_text = Text(decision_frame, height=5, width=60)
    data_sources_text.grid(column=1, row=0)

    ttk.Label(decision_frame, text="Data sinks: ").grid(column=0, row=1, sticky="W")
    data_sinks_text = Text(decision_frame, height=5, width=60)
    data_sinks_text.grid(column=1, row=1)

    ttk.Label(decision_frame, text="Processing: ").grid(column=0, row=2, sticky="W")
    processing_text = Text(decision_frame, height=5, width=60)
    processing_text.grid(column=1, row=2)

    ttk.Label(subroot, text="Communication: ").grid(column=0, row=3, sticky="W")
    communication_text = Text(subroot, height=5, width=60)
    communication_text.grid(column=1, row=3)

    ttk.Label(subroot, text="Interfaces: ").grid(column=0, row=4, sticky="W")
    interfaces_text = Text(subroot, height=5, width=60)
    interfaces_text.grid(column=1, row=4)

    ttk.Label(subroot, text="Rationale: ").grid(column=0, row=5, sticky="W")
    rationale_text = Text(subroot, height=5, width=60)
    rationale_text.grid(column=1, row=5)

    ttk.Label(subroot, text="Consequences: ").grid(column=0, row=6, sticky="W")
    consequences_text = Text(subroot, height=6, width=60)
    consequences_text.grid(column=1, row=6)

    ttk.Label(subroot, text="References: ").grid(column=0, row=7, sticky="W")
    references_text = Text(subroot, height=6, width=60)
    references_text.grid(column=1, row=7)

    save_button = ttk.Button(subroot, text="Save", command=save_input)
    save_button.grid(column=1, row=8)



def event_based_template():
    def save_input():
        with open("event_based_style_adr.md", "w") as f:
            f.write(f"Status: {status_text.get(1.0, END)}")
            f.write(f"Context: {context_text.get(1.0, END)}")
            f.write(f"Decision:\n")
            f.write(f"  Event Emitters: {event_emitters_text.get(1.0, END)}")
            f.write(f"  Event Listeners: {event_listeners_text.get(1.0, END)}")
            f.write(f"  Event Channels: {event_channels_text.get(1.0, END)}")
            f.write(f"Rationale: {rationale_text.get(1.0, END)}")
            f.write(f"Consequences: {consequences_text.get(1.0, END)}")
            f.write(f"References: {references_text.get(1.0, END)}")

    subroot = Tk()
    subroot.title("Event-based Style ADR")

    # Create labels and text boxes for each section of the template
    ttk.Label(subroot, text="Status: ").grid(column=0, row=0, sticky="W")
    status_text = Text(subroot, height=2, width=60)
    status_text.grid(column=1, row=0)

    ttk.Label(subroot, text="Context: ").grid(column=0, row=1, sticky="W")
    context_text = Text(subroot, height=5, width=60)
    context_text.grid(column=1, row=1)

    ttk.Label(subroot, text="Decision: ").grid(column=0, row=2, sticky="W")
    decision_frame = ttk.Frame(subroot, padding=10)
    decision_frame.grid(column=1, row=2)

    ttk.Label(decision_frame, text="Event Emitters: ").grid(column=0, row=0, sticky="W")
    event_emitters_text = Text(decision_frame, height=5, width=60)
    event_emitters_text.grid(column=1, row=0)

    ttk.Label(decision_frame, text="Event Listeners: ").grid(column=0, row=1, sticky="W")
    event_listeners_text = Text(decision_frame, height=5, width=60)
    event_listeners_text.grid(column=1, row=1)

    ttk.Label(decision_frame, text="Event Channels: ").grid(column=0, row=2, sticky="W")
    event_channels_text = Text(decision_frame, height=5, width=60)
    event_channels_text.grid(column=1, row=2)

    ttk.Label(subroot, text="Rationale: ").grid(column=0, row=3, sticky="W")
    rationale_text = Text(subroot, height=5, width=60)
    rationale_text.grid(column=1, row=3)

    ttk.Label(subroot, text="Consequences: ").grid(column=0, row=4, sticky="W")
    consequences_text = Text(subroot, height=5, width=60)
    consequences_text.grid(column=1, row=4)

    ttk.Label(subroot, text="References: ").grid(column=0, row=5, sticky="W")
    references_text = Text(subroot, height=5, width=60)
    references_text.grid(column=1, row=5)

    save_button = ttk.Button(subroot, text="Save", command=save_input)
    save_button.grid(column=1, row=6)
