# 466-adr-gen
A command line (pipe-and-filter) tool to assist with the generation of Architectural Decision Records.

# Setup
Make sure the .exe file (adr-gen.exe) is in the /bin/ directory of one of the shells you use for your general workflow.

# Dev Env Setup
1. `pip install` pyinstaller
2. Use `pyinstaller -F /path/to/adr-gen.py` to compile the Python code into a single executable
3. Test the executable by running it in your shell