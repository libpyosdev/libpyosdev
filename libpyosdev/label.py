"""
Module for label management
"""

from functools import wraps

def label(name: str | None = None):
    """
    Define a label and generate it when called
    - `name`                : name of label
    """

    def decorator(func):
        label_name = name or func.__name__

        @wraps(func)
        def wrapper(self, *args, **kwargs):
            self.generate_line(f"{label_name}:")
            return func(self, *args, **kwargs)

        wrapper._is_label = True
        wrapper._label_name = label_name

        return wrapper

    if callable(name):
        func = name
        return decorator(func)

    return decorator