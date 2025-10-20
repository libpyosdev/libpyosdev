"""
Module to implement BIOS functions wrappers for your architecture
"""

class BIOS:
    """
    Represents a generic BIOS
    """

    def __init__(self):
        self.asm = None
        self.regs = None
        self.interrupt_table = {}

    def interrupt(self, intno: int, *args):
        """
        Generate wrappers for interrupts.
        When implementing a BIOS class, you should create a function for each supported interrupt
        and call these functions here.
        """

        raise NotImplementedError()