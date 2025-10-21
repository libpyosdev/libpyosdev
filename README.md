# LibPyOSDev

## What?
LibPyOSDev is a free and open-source modern Python library for operating system development. The goal is to provide a set of modules, classes and functions to help people coding their own operating system in a Pythonic way.

## How?
LibPyOSDev does not make you code an operating system in Python, but uses Python to generate Assembly code. The result is pure text, and Python does not run directly on your CPU.

## Features
- Intel x86 8086 architecture support
- Architecture package template
- CPU registers representations for debugging
- Programs management

## Installation
**Step 1:** clone this repository
```sh
git clone https://github.com/libpyosdev/libpyosdev
```

**Step 2:** make sure that all the requirements below are installed on your system:
- Python 3.11+
- pip
- NASM (if you want to assemble the generated code)

**Step 3:** run `pip` in the library directory. Make sure you are using a Python virtual environment.
```sh
# create the virtual environment
python -m venv venv
source venv/bin/activate

# install LibPyOSDev
pip install .
```

Now, LibPyOSDev should be installed! You can try it by importing it:
```py
import libpyosdev
```

## Contributing
You can read the contributing guide [here](CONTRIBUTING.md).

## Documentation
The full documentation is available [here](https://pyosdevlib.github.io/pyosdevlib).