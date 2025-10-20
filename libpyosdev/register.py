"""
Module for debugging registers
"""

from typing import Any

class Register:
    """
    Represents a CPU register.
    Note that this class is only for debugging and does not interact with real CPU registers.
    - `name`                        : name of register
    - `size`                        : size of register (8, 16, 32, 64)
    - `value`                       : value of register
    """

    def __init__(self, name: str, size: int, value: Any=0):
        self.name = name
        self.size = size
        self.value = value

    def symbol(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"<Register {self.name} ({self.size}-bit) = {self.value}>"