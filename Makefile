# Define the PyInstaller command and any options
PYINSTALLER_CMD = pyinstaller
PYINSTALLER_OPTS = -F

# Define the target executable file
TARGET = adr-gen

# Define the path to the Python script
PY_SRC = ./$(TARGET).py

# Build the executable with PyInstaller
pyinstaller:
	$(PYINSTALLER_CMD) $(PYINSTALLER_OPTS) $(PY_SRC)

# Run the executable
run:
	./dist/$(TARGET); exit;

# Clean up the PyInstaller build artifacts
clean:
	rm -rf dist/$(TARGET) $(TARGET).spec