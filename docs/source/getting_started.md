# Getting started
---
## Summary
- [How does it work?](#how-does-it-work)
- [Installation](#installation)
- [Testing](#testing)

## How does it work?
LibPyOSDev **does not** make you code an operating system **in Python**, but **uses Python to generate Assembly code**. The result is pure text, and Python does not run directly on your CPU. It can be described as a kind of very advanced preprocessor.

## Installation
**Step 1:** clone the repository
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

## Testing
Now, let's see if the library has been installed successfully:
```sh
python
>>> import libpyosdev
```
It should not display an error.