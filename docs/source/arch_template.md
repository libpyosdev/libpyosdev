# Architecture template
---
## Summary
- [The `arch` package](#the-arch-package)
- [Architecture informations](#architecture-informations)
- [Registers](#registers)
- [Instructions](#instructions)
- [BIOS](#bios)

## The "arch" package
LibPyOSDev provides a package named `arch`. It provides module templates to help you add support for your architecture.
- `infos`: informations about the architecture
- `registers`: representation of the architecture CPU registers
- `instructions`: architecture CPU instruction set
- `bios`: representation of the architecture BIOS (if supported) and wrappers to its functions

## Architecture informations
The `arch.infos` module contains the `ArchitectureInfos` class, used to represent architectures. It is defined as described below:
```py
ArchitectureInfos(
    name: str,
    bits: int,
    max_mem: int,
    registers: TInstr,
    instructions: TRegs,
    bios: BIOS
)
```
The `name` parameter is the name of the architecture. \
The `bits` parameter is the size of a word on the architecture (e.g. 16, 32, 64, ...). \
The `max_men` parameter is the maximum amount of RAM that can be handled by the architecture. \
The `registers` parameter represents to the architecture registers. \
The `instructions` parameter represents the architecture instructions. \
The `bios` parameter represents the architecture BIOS (`None` if it is not supported)

The `__repr__()` method returns the following text:
```
<Architecture NAME (BITS-bit) max memory: MAX_MEM>
```

## Registers
The `arch.registers` module contains a generic class named `RegistersArch` to regroup the architecture CPU registers.

## Instructions
The `arch.instructions` module contains two classes: `GenericInstruction` and `ArchInstructions`. The first one represents a specific instruction. The second one regroups the instances of `GenericInstruction`.
```py
GenericInstruction(
    mnemonic: str,
    operand_count: int
)
```
The `mnemonic` parameter represents the name of the instruction (e.g. mov). \
The `operand_count` parameter represents the number of operands that is required (e.g. 2).

When an instance of this class is called, it generates the corresponding Assembly code using the `emit()` function, called automatically by `__call__()`.

`ArchInstructions` has the `link_program()` method, to tell the instructions in which program they must emit their code.

## BIOS
The `arch.bios` module contains the `BIOS` class, which represents the BIOS of the architecture. This class uses a dictionnary named `interrupt_table`
```
interrupt number: interrupt wrapper
```
and a function named `interrupt()`:
```py
interrupt(
    intno: int,
    *args
)
```
The `intno` parameter is the number of the interrupt (not the real number but the number defined in the BIOS class).
The `args` parameter is the values needed by the interrupt. They must be given **in order** and are moved to registers.