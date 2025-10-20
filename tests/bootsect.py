from libpyosdev.program import Program
from libpyosdev.x86_8086.infos import info8086
from libpyosdev.label import Label

class BootSector(Program):
    def __init__(self):
        super().__init__("bootsect", info8086, "tests/output/bootsect.asm")
        self.start = Label("start")

    def _1_informations(self):
        self.asm.org(0x7C00)

    def _2_start(self):
        self.generate_line(self.start())
        self.asm.xor(self.regs.AX, self.regs.AX)
        self.asm.mov(self.regs.DS, self.regs.AX)
        self.asm.mov(self.regs.ES, self.regs.AX)
        self.asm.mov(self.regs.SS, self.regs.AX)
        self.asm.mov(self.regs.SP, 0xF000)

        self.bios.interrupt(self.bios.SET_VIDEO_MODE, 0x03)
        self.bios.interrupt(self.bios.RESET_DISK)
        self.bios.interrupt(self.bios.TELETYPE_PUTCHAR, ord('A'), 0, 0x0F)

        self.asm.hlt()
        self.asm.jmp(self.asm.CURRENT_ADDRESS)

    def _3_sign(self):
        self.code.append("times 510 - ($ - $$) db 0")
        self.asm.dw(0xAA55)

    def run(self):
        self.write()

bootsect = BootSector()
bootsect.run()