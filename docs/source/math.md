# Maths
---
## Summary
- [Get physical addresses in real mode](#real-mode-physical-addresses)

## Real mode physical addresses
To get a physical address in real mode, you need to do this operation:
```
offset * 16 + segment
```
The `libpyosdev.math` module provides a function to perform this operation.
```py
realmode_physaddr(
    offset: int,
    segment: int
)
```