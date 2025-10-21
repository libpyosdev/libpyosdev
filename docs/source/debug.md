# Debugging
---
## Summary
- [Debugging registers](#debugging-registers)

## Debugging registers
LibPyOSDev provides powerful debugging features. The `register` module provides the `Register` class, which is used to represent CPU registers.
```py
Register(
    name: str,
    size: str,
    value: Any=0
)
```
The `name` parameter is the name of the register (e.g. AX, BX, SI, CS, ...). \
The `size` parameter is the size of the register (e.g. 1, 8, 16, 32, 64). \
The `value` parameter is the value of the register, set to 0 by default. **The class is not linked with CPU registers, so you need to update the value yourself after an operation if you want to get it.**

To access a register, you can use the `Register.symbol()` method which returns its name. However, this function is called automatically so you are not forced to call it.

The `__repr__()` method returns this representation:
```
<Register NAME (SIZE-bit) = VALUE>
```