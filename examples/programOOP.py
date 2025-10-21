from libpyosdev.program import Program
from libpyosdev.x86_8086.infos import info8086

class MyProgram(Program):
    def __init__(self):
        super().__init__("my_program", info8086, output="examples/output/my_program.asm")

    def run(self):
        self.generate_line("mov ax, 0x1234")
        self.generate_line("mov bx, ax")

        self.write()

myprog = MyProgram()
myprog.run()