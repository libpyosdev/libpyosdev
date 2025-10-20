from libpyosdev.program import Program
from libpyosdev.x86_8086.infos import info8086

program = Program("instructions", info8086, "tests/output/instructions.asm")

program.asm.mov(program.regs.AX, 50)

program.write()