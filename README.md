# 466-adr-gen
A command line (pipe-and-filter) tool to assist with the generation of Architectural Decision Records.

# Setup
Make sure the .exe file (adr-gen.exe) is in the /bin/ directory of one of the shells you use for your general workflow.

# Dev Env Setup
1. `pip install` pyinstaller
2. Use `pyinstaller -F /path/to/adr-gen.py` to compile the Python code into a single executable
3. Test the executable by running it in your shell
    - With Git Bash, you can put the .exe file (along with any of your most-used templates) in your /usr/bin/ directory to use the tool.

## makefile
When using the Makefile, make sure you are in the current directory.
run `make` to compile the python file into an executable.
run `make run` to run the following program.
run `make clean` to removed the compiled python files.