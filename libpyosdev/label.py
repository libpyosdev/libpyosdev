"""
Module to manage labels
"""

class Label:
    """
    Represents a label
    - `name`                        : name of label
    """

    def __init__(self, name: str):
        self.name = name

    def __call__(self) -> str:
        return f"{self.name}:"