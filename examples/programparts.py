from libpyosdev.program import Program
from libpyosdev.x86_8086.infos import info8086

class MyProgram(Program):
    def __init__(self):
        super().__init__("my_program", info8086, output="examples/output/program_parts.asm")

    def _1_first_step(self):
        self.generate_line("start:")
        self.generate_line("    mov ax, 10")
        self.generate_line("    mov bx, 5")
        self.generate_line("    add ax, bx")
        self.generate_line("    jmp hang")

    def _2_second_step(self):
        self.generate_line("hang:")
        self.generate_line("    jmp hang")

    def run(self):
        self.write()

myprog = MyProgram()
myprog.run()