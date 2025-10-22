"""
A 8086 kernel preset
"""

from libpyosdev import label
from libpyosdev.presets.x86_8086.constants import KERNEL_LOAD_ADDR
from libpyosdev.program import Program, part
from libpyosdev.x86_8086.infos import info8086

class x86_8086_Kernel(Program):
    def __init__(self, output: str="x86_8086_kernel.asm"):
        super().__init__("x86_8086_kernel", info8086, output)

    @label()
    def start(self):
        self.asm.xor(self.regs.AX, self.regs.AX)
        self.asm.mov(self.regs.DS, self.regs.AX)
        self.asm.mov(self.regs.ES, self.regs.AX)
        self.asm.mov(self.regs.SS, self.regs.AX)
        self.asm.mov(self.regs.SP, 0xF000)

        self.asm.hlt()
        self.asm.jmp(self.asm.CURRENT_ADDRESS)

    @part(1)
    def setup(self):
        self.asm.org(KERNEL_LOAD_ADDR)

    @part(2)
    def body(self):
        self.start()

    def run(self):
        self.write()