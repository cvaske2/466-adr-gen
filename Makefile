# Define the PyInstaller command and any options
PYINSTALLER_CMD = pyinstaller
PYINSTALLER_OPTS = -F

# Define the target executable file
TARGET = adr-gen

# Define the path to the Python script
PY_SRC = ./adr-gen.py

# Build the executable with PyInstaller
pyinstaller:
	$(PYINSTALLER_CMD) $(PYINSTALLER_OPTS) $(PY_SRC)

# Run the executable
run:
	~/git/466-adr-gen/dist/adr-gen; exit;

# Clean up the PyInstaller build artifacts
clean:
	rm -rf build/ dist/ $(TARGET)