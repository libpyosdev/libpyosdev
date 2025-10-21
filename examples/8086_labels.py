from libpyosdev.program import Program
from libpyosdev.label import label
from libpyosdev.x86_8086.infos import info8086

class Labels8086(Program):
    def __init__(self):
        super().__init__("8086_labels", info8086, "examples/output/8086_labels.asm")

    @label()
    def start(self):
        self.asm.mov(self.regs.AX, 2)
        self.asm.add(self.regs.AX, 4)
        self.asm.jmp("loop")

    @label()
    def loop(self):
        self.asm.inc(self.regs.AX)
        self.asm.cmp(self.regs.AX, 10)
        self.asm.jne("loop")

    def _1_body(self):
        self.start()
        self.loop()

    def run(self):
        self.write()

prog = Labels8086()
prog.run()