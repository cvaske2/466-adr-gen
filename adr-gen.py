import sys
from tkinter import *
from tkinter import ttk

def split_string(template_string):
    '''
    Split the string template that has been read from the file into a dictionary.
    Dictionary is of the form
    {
        heading1: "<template content suggestion>",
        heading2: "",
        heading3: "<template content suggestion>",
        ...
    }
    '''
    START = "**"
    END = ":**"
    result = dict()

    for line in template_string.splitlines():
        try:
            start_index = line.index(START) + len(START)
            end_index = line.index(END, start_index)
            section_header = line[start_index:end_index]

            remainder = line[end_index + len(END):]
            result[section_header] = remainder
        except ValueError:
            continue
    return result

def open_style_template(template_path):
    '''
    Open the file and split the string
    Returns a dictionary
    '''
    with open(template_path) as file:
        data = file.read()
    return split_string(data)

def open_window(template_data):
    '''
    Opens a window and adds content based on the data read from the template.
    Parameter: "template_data" - a diciontary of the form { heading: "<template content suggestion>", ... }
    Returns: nothing (right now). Opens a tkinter window with the template content

    Issue: checking a single checkbox changes all of the checkboxes. Need to look into this.
    '''
    subroot = Tk()
    #subroot = window
    subroot.title("Template item select")

    new_frame = ttk.Frame(subroot, padding=10)
    new_frame.grid()
    
    row_index = 0
    heading_flags = []

    for heading in template_data:
        heading_flags.append(1)

        ttk.Label(new_frame, text=f'{heading}: ').grid(column=0, row=row_index)
        ttk.Checkbutton(new_frame, variable=heading_flags[row_index], onvalue=1, offvalue=0).grid(column=1, row=row_index)
        row_index += 1

def open_cs():
    '''
    Opens a window and adds content based on the data read from the template.
    Parameter: "template_data" - a dictionary of the form { heading: "<template content suggestion>", ... }
    Returns: nothing (right now). Opens a tkinter window with the template content
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




def open_client_server_style():
    template_content = open_style_template("./adr-templates/client-server-style.md")
    open_window(template_content)

def open_data_flow_style():
    template_content = open_style_template("./adr-templates/data-flow-style.md")
    open_window(template_content)

def open_event_based_style():
    template_content = open_style_template("./adr-templates/event-based-style.md")
    open_window(template_content)

def open_layered_style():
    template_content = open_style_template("./adr-templates/layered-style.md")
    open_window(template_content)

def open_main_program_and_subroutine_style():
    template_content = open_style_template("./adr-templates/main-program-and-subroutine-style.md")
    open_window(template_content)

def open_object_oriented_style():
    template_content = open_style_template("./adr-templates/object-oriented-style.md")
    open_window(template_content)

def open_peer_to_peer_style():
    template_content = open_style_template("./adr-templates/peer-to-peer-style.md")
    open_window(template_content)

def open_pipe_and_filter_style():
    template_content = open_style_template("./adr-templates/pipe-and-filter-style.md")
    open_window(template_content)

def open_publish_subscribe_style():
    template_content = open_style_template("./adr-templates/publish-subscribe-style.md")
    open_window(template_content)

def open_rule_based_style():
    template_content = open_style_template("./adr-templates/rule-based-style.md")
    open_window(template_content)

def create_new_window():
    open_cs()


# Grab args and slice off first (name of executable)
ARGS = sys.argv[1:]


if len(ARGS) != 0 and ARGS[0] in ['help', '-help', '--help', '-h', '--h']:
    print("Here are some parameters available to you:") # TODO: implement
    print()
    exit()

root = Tk()
frame = ttk.Frame(root, padding=10)
frame.grid()

root.title("Template Select")

ttk.Label(frame, text="Select from a style template").grid(column=0, row=0)
ttk.Button(frame, text="Client Server Style", command=open_client_server_style).grid(column=0, row=1)
ttk.Button(frame, text="Data Flow", command=open_data_flow_style).grid(column=0, row=2)
ttk.Button(frame, text="Event Based", command=open_event_based_style).grid(column=0, row=3)
ttk.Button(frame, text="Layered Style", command=open_layered_style).grid(column=0, row=4)
ttk.Button(frame, text="Main Program & Subroutine Style", command=open_main_program_and_subroutine_style).grid(column=0, row=5)
ttk.Button(frame, text="Object Oriented Style", command=open_object_oriented_style).grid(column=0, row=6)
ttk.Button(frame, text="Peer to Peer Style", command=open_peer_to_peer_style).grid(column=0, row=7)
ttk.Button(frame, text="Pipe and Filter Style", command=open_pipe_and_filter_style).grid(column=0, row=8)
ttk.Button(frame, text="Publish/Subscribe Style", command=open_publish_subscribe_style).grid(column=0, row=9)
ttk.Button(frame, text="Rule-Based Style", command=open_rule_based_style).grid(column=0, row=10)
ttk.Button(frame, text="Client Server Style", command=lambda: create_new_window()).grid(column=0, row=11)


root.mainloop()
