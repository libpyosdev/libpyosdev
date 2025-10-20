"""
Informations about the 8086 architecture
"""

from libpyosdev.arch.infos import ArchitectureInfos
from libpyosdev.x86_8086.bios import BIOS_8086
from libpyosdev.x86_8086.instructions import Instr8086
from libpyosdev.x86_8086.registers import Registers8086

info8086 = ArchitectureInfos("x86_8086", 16, 1024*1024, Registers8086(), Instr8086(), BIOS_8086())