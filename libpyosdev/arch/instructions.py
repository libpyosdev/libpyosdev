"""
Instructions supported by your architecture
"""

from libpyosdev.register import Register

class GenericInstruction:
    """
    Represents an instruction
    - `mnemonic`                    : mnemonic of instruction
    - `operand_count`               : number of operands required by the instruction
    - `emit()`                      : compiles the instruction
    """

    def __init__(self, mnemonic: str, operand_count: int):
        self.mnemonic = mnemonic
        self.operand_count = operand_count
        self._program = None

    def __repr__(self) -> str:
        return f"<Instruction {self.mnemonic} requires {self.operand_count} operands>"

    def __call__(self, *operands):
        if self._program is None:
            raise RuntimeError(f"Instruction {self.mnemonic} is not linked to a program")
        self.emit(*operands, program=self._program)

    def emit(self, *operands, program) -> None:
        """
        Emit the Assembly code
        """

        if len(operands) != self.operand_count:
            raise ValueError(f"Instruction {self.mnemonic} requires {self.operand_count} operands but got {len(operands)}")
        operands_str = [op.symbol() if isinstance(op, Register) else str(op) for op in operands]
        line = f"{self.mnemonic} {', '.join(operands_str)}"
        program.generate_line(line)

class ArchInstructions:
    """
    Architecture instructions should be regrouped here
    """

    def __init__(self, program=None):
        pass

    def link_program(self, program):
        """
        Link a program to instructions
        """

        for instr in vars(self).values():
            if isinstance(instr, GenericInstruction):
                instr._program = program