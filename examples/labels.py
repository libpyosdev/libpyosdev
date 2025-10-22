from libpyosdev.program import Program, part
from libpyosdev.label import label
from libpyosdev.x86_8086.infos import info8086

class UsingLabels(Program):
    def __init__(self):
        super().__init__("using_labels", info8086, "examples/output/using_labels.asm")

    @label()
    def start(self):
        self.generate_line("    mov ax, 10")
        self.generate_line("    mov bx, 25")
        self.generate_line("    add bx, ax")
        self.generate_line("    mov dx, bx")

    @label(name="substract")
    def label2(self):
        self.generate_line("    mov ax, 8")
        self.generate_line("    mov bx, 7")
        self.generate_line("    sub ax, bx")

    @part(1)
    def body(self):
        self.start()
        self.generate_line("    jmp label2")
        self.label2()

    def run(self):
        self.write()

prog = UsingLabels()
prog.run()