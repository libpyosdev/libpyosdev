"""
8086 registers
"""

from libpyosdev.arch.registers import RegistersArch
from libpyosdev.register import Register

class Registers8086(RegistersArch):
    """
    8086 CPU registers:
    AX, AH, AL, BX, BH, BL, CX, CH, CL, DX, DH, DL, SP, BP, SI, DI, CS, DS, ES, SS, IP,
    FLAGS, CF, PF, AF, ZF, SF, TF, IF, DF, OF
    """

    AX = Register("ax", 16)
    AH = Register("ah", 8)
    AL = Register("al", 8)

    BX = Register("bx", 16)
    BH = Register("bh", 8)
    BL = Register("bl", 8)

    CX = Register("cx", 16)
    CH = Register("ch", 8)
    CL = Register("cl", 8)

    DX = Register("dx", 16)
    DH = Register("dh", 8)
    DL = Register("dl", 8)

    SP = Register("sp", 16)
    BP = Register("bp", 16)
    SI = Register("si", 16)
    DI = Register("di", 16)

    CS = Register("cs", 16)
    DS = Register("ds", 16)
    ES = Register("es", 16)
    SS = Register("ss", 16)

    IP = Register("ip", 16)

    FLAGS = Register("flags", 16)
    CF = Register("cf", 1)
    PF = Register("pf", 1)
    AF = Register("af", 1)
    ZF = Register("zf", 1)
    SF = Register("sf", 1)
    TF = Register("tf", 1)
    IF = Register("if", 1)
    DF = Register("df", 1)
    OF = Register("of", 1)