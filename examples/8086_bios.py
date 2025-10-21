from libpyosdev.program import Program
from libpyosdev.x86_8086.infos import info8086

prog = Program("8086_bios", info8086, output="examples/output/8086_bios.asm")

prog.bios.interrupt(prog.bios.TELETYPE_PUTCHAR, ord('A'), 0, 0x0F)

prog.write()