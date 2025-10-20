from libpyosdev.program import Program
from libpyosdev.x86_8086.registers import Registers8086

program = Program("registers", "tests/output/registers.asm")

print(Registers8086.AX)
program.generate_line("mov ax, 50")
Registers8086.AX.value = 50
print(Registers8086.AX)

program.write()