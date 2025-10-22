## Version 0.1.2
- Fiex `Program.generate_preamble()` (replaced "pyosdevlib" by "libpyosdev")
- Fixed presets by using `parts`

## Version 0.1.1
- Updated documentation
    - Programs management section now explains `parts`
    - Added section about full 8086 support
- Added `part` decorator
- Added `math` module:
    - Added `realmode_physaddr()`
- Added `presets` package
    - Added `presets.x86_8086` package
        - Added `presets.x86_8086.bootloader` module
        - Added `presets.x86_8086.kernel` module
    - Added `presets.constants` module
        - BOOTSECT_LOAD_ADDR
        - MBR_BOOTSECT_SIGNATURE

## Version 0.1.0
- Changed version to 0.1.0 because hatchling may not support it

## Version 0.0.0
- Added architecture template
- Added CPU register representations for debugging
- Added Intel x86 8086 support
- Added extensible packages, modules and classes