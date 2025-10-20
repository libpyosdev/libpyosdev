from libpyosdev.program import Program
from libpyosdev.x86_8086.infos import info8086

program = Program("architecture", "tests/output/architecture.asm")

print(info8086)

program.write()