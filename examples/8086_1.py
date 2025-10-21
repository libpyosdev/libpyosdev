from libpyosdev.program import Program
from libpyosdev.x86_8086.infos import info8086

prog = Program("8086_program", info8086, "examples/output/8086_program.asm")

prog.asm.mov(prog.regs.AX, 0x28)
prog.asm.mov(prog.regs.BX, prog.regs.AX)
prog.asm.add(prog.regs.AX, prog.regs.BX)

prog.write()