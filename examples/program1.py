from libpyosdev.program import Program
from libpyosdev.x86_8086.infos import info8086

prog = Program("first_program", info8086, output="examples/output/first_program.asm")

prog.generate_line("mov ax, 0x1234")
prog.generate_line("mov bx, ax")

prog.write()