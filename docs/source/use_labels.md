# Using labels
---
## Summary
- [What is a label?](#what-is-a-label)
- [Defining labels](#defining-labels)

## What is a label?
**Reminder:** a label is a point in the code used to refer easily to a part. In modern languages, they are replaced by conditions and loops strctures, but they are still used in Assembly languages.

## Defining labels
Instead of defining labels using raw Assembly lines, LibPyOSDev contains a module named `label` which provides the `label` decorator.
```py
@label(
    name: str
)
```
The name of the label can be defined in two different ways. \
The first way is to set the `name` parameter manually.
```py
@label(name="example_label")
def example_label():
    pass
```
The second way is to let `name` empty. Then, the name of the label will be the name of the decorated function.
```py
@label()
def example_label():
    pass
```
If you use the first method, the value of `name` will be used instead of the function name.

Once your labels are defined, you can call them in your program. If you don't call their associated functions, they will never be generated.