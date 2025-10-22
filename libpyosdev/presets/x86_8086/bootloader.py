"""
A MBR 8086 bootloader preset
"""

from libpyosdev.label import label
from libpyosdev.program import Program
from libpyosdev.x86_8086.infos import info8086
from libpyosdev.presets.x86_8086.constants import BOOTSECT_LOAD_ADDR, MBR_BOOTSECT_SIGNATURE

class x86_8086_Bootloader(Program):
    def __init__(self, output: str="x86_8086_bootloader.asm", kbase: int=0x100, ksize: int=1):
        super().__init__("x86_8086_bootloader", info8086, output)
        self.kbase = kbase
        self.ksize = ksize

    @label()
    def start(self):
        self.asm.xor(self.regs.AX, self.regs.AX)
        self.asm.mov(self.regs.DS, self.regs.AX)
        self.asm.mov(self.regs.ES, self.regs.AX)
        self.asm.mov(self.regs.SS, self.regs.AX)
        self.asm.mov(self.regs.SP, 0xF000)

        self.bios.interrupt(self.bios.READ_SECTORS, self.ksize, 0, 2, 0, "[driveno]", 0, self.kbase)

        self.asm.jmp(f"{self.kbase}:0")

        self.asm.hlt()
        self.asm.jmp(self.asm.CURRENT_ADDRESS)

    def _1_setup(self):
        self.asm.org(BOOTSECT_LOAD_ADDR)

    def _2_body(self):
        self.start()

    def _3_data(self):
        @label()
        def driveno(self):
            self.asm.db(0)

        driveno(self)

    def _4_end(self):
        self.generate_line(f"times 510 - ({self.asm.CURRENT_ADDRESS} - {self.asm.SEGMENT_START}) db 0")
        self.asm.dw(MBR_BOOTSECT_SIGNATURE)

    def run(self):
        self.write()