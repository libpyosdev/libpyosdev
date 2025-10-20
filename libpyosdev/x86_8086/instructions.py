"""
8086 general instructions
"""

from libpyosdev.arch.instructions import ArchInstructions, GenericInstruction

class Instr8086(ArchInstructions):
    """
    Contains 8086 general instructions
    """

    def __init__(self, program=None):
        self.CURRENT_ADDRESS = "$"
        self.SEGMENT_START = "$$"

        self.comment = GenericInstruction(";", 1)

        self.org = GenericInstruction("org", 1)

        self.db = GenericInstruction("db", 1)
        self.dw = GenericInstruction("dw", 1)
        self.resb = GenericInstruction("resb", 1)
        self.resw = GenericInstruction("resw", 1)

        self.mov = GenericInstruction("mov", 2)
        self.xchg = GenericInstruction("xchg", 2)
        self.lea = GenericInstruction("lea", 2)
        self.lds = GenericInstruction("lds", 2)
        self.les = GenericInstruction("les", 2)
        self.lahf = GenericInstruction("lahf", 0)
        self.sahf = GenericInstruction("sahf", 0)
        self.push = GenericInstruction("push", 1)
        self.pop = GenericInstruction("pop", 1)
        self.pushf = GenericInstruction("pushf", 0)
        self.popf = GenericInstruction("popf", 0)

        self.add = GenericInstruction("add", 2)
        self.adc = GenericInstruction("adc", 2)
        self.sub = GenericInstruction("sub", 2)
        self.sbb = GenericInstruction("sbb", 2)
        self.inc = GenericInstruction("inc", 1)
        self.dec = GenericInstruction("dec", 1)
        self.mul = GenericInstruction("mul", 1)
        self.imul = GenericInstruction("imul", 1)
        self.imul2 = GenericInstruction("imul", 2)
        self.div = GenericInstruction("div", 1)
        self.idiv = GenericInstruction("idiv", 1)
        self.neg = GenericInstruction("neg", 1)
        self.cmp = GenericInstruction("cmp", 2)

        self.not_ = GenericInstruction("not", 1)
        self.and_ = GenericInstruction("and", 2)
        self.or_ = GenericInstruction("or", 2)
        self.xor = GenericInstruction("xor", 2)
        self.test = GenericInstruction("test", 2)
        self.shl = GenericInstruction("shl", 2)
        self.sal = GenericInstruction("sal", 2)
        self.shr = GenericInstruction("shr", 2)
        self.sar = GenericInstruction("sar", 2)
        self.rol = GenericInstruction("rol", 2)
        self.ror = GenericInstruction("ror", 2)
        self.rcl = GenericInstruction("rcl", 2)
        self.rcr = GenericInstruction("rcr", 2)

        self.jmp = GenericInstruction("jmp", 1)
        self.call = GenericInstruction("call", 1)
        self.ret = GenericInstruction("ret", 0)
        self.ret1 = GenericInstruction("ret", 1)
        self.je = GenericInstruction("je", 1)
        self.jz = GenericInstruction("jz", 1)
        self.jne = GenericInstruction("jne", 1)
        self.jnz = GenericInstruction("jnz", 1)
        self.jl = GenericInstruction("jl", 1)
        self.jle = GenericInstruction("jle", 1)
        self.jg = GenericInstruction("jg", 1)
        self.jge = GenericInstruction("jge", 1)
        self.jnle = GenericInstruction("jnle", 1)
        self.jnge = GenericInstruction("jnge", 1)
        self.jng = GenericInstruction("jng", 1)
        self.jc = GenericInstruction("jc", 1)
        self.jnc = GenericInstruction("jnc", 1)
        self.jo = GenericInstruction("jo", 1)
        self.jno = GenericInstruction("jno", 1)
        self.js = GenericInstruction("js", 1)
        self.jns = GenericInstruction("jns", 1)
        self.loop = GenericInstruction("loop", 1)
        self.loope = GenericInstruction("loope", 1)
        self.loopz = GenericInstruction("loopz", 1)
        self.loopne = GenericInstruction("loopne", 1)
        self.loopnz = GenericInstruction("loopnz", 1)
        self.jcxz = GenericInstruction("jcxz", 1)

        self.movsb = GenericInstruction("movsb", 0)
        self.movsw = GenericInstruction("movsw", 0)
        self.lodsb = GenericInstruction("lodsb", 0)
        self.lodsw = GenericInstruction("lodsw", 0)
        self.stosb = GenericInstruction("stosb", 0)
        self.stosw = GenericInstruction("stosw", 0)
        self.scasb = GenericInstruction("scasb", 0)
        self.scasw = GenericInstruction("scasw", 0)
        self.cmpsb = GenericInstruction("cmpsb", 0)
        self.cmpsw = GenericInstruction("cmpsw", 0)

        self.clc = GenericInstruction("clc", 0)
        self.stc = GenericInstruction("stc", 0)
        self.cli = GenericInstruction("cli", 0)
        self.sti = GenericInstruction("sti", 0)
        self.cld = GenericInstruction("cld", 0)
        self.std = GenericInstruction("std", 0)
        self.nop = GenericInstruction("nop", 0)
        self.hlt = GenericInstruction("hlt", 0)
        self.wait = GenericInstruction("wait", 0)
        self.esc = GenericInstruction("esc", 1)
        self.int_ = GenericInstruction("int", 1)
        self.int3 = GenericInstruction("int3", 0)
        self.iret = GenericInstruction("iret", 0)

        self.link_program(program)