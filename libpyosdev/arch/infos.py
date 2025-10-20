"""
Informations about your architecture
"""

from typing import Generic, TypeVar
from libpyosdev.arch.bios import BIOS
from libpyosdev.arch.instructions import ArchInstructions
from libpyosdev.arch.registers import RegistersArch

TRegs = TypeVar("TRegs", bound=RegistersArch)
TInstr = TypeVar("TInstr", bound=ArchInstructions)

class ArchitectureInfos(Generic[TRegs, TInstr]):
    """
    Generic class that gives informations about an architecture
    - `name`                            : name of architecture
    - `bits`                            : bits of architecture (8, 16, 32, 64)
    - `max_men`                         : the maximum amount of RAM handled by the architecture
    """

    def __init__(self, name: str, bits: int, max_mem: int, registers: TInstr, instructions: TRegs, bios: BIOS):
        self.name = name
        self.bits = bits
        self.max_mem = max_mem
        self.registers = registers
        self.instructions = instructions
        self.bios = bios
        self.bios.asm = self.instructions
        self.bios.regs = self.registers

    def __repr__(self) -> str:
        return f"<Architecture {self.name} ({self.bits}-bit) max memory: {self.max_mem}>"