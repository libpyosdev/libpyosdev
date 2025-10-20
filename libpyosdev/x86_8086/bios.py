"""
8086 BIOS
"""

from libpyosdev.arch.bios import BIOS

class BIOS_8086(BIOS):
    """
    Represents the 8086 BIOS
    """

    SET_VIDEO_MODE              = 0
    SET_CURSOR_POS              = 1
    GET_CURSOR_POS              = 2
    PUTCHAR                     = 3
    TELETYPE_PUTCHAR            = 4
    GET_VIDEO_MODE              = 5
    GET_SHIFT_FLAGS             = 6
    RESET_DISK                  = 7
    READ_SECTORS                = 8
    WRITE_SECTORS               = 9
    GET_DRIVE_PARAMS            = 10
    CHECK_MEMORY                = 11
    GET_MEMORY_SIZE             = 12
    QUERY_MEMORY                = 13
    GET_TIME                    = 14
    SET_TIME                    = 15

    def __init__(self):
        super().__init__()

        self.interrupt_table = {
            self.SET_VIDEO_MODE             : self.set_video_mode,
            self.SET_CURSOR_POS             : self.set_cursor_pos,
            self.GET_CURSOR_POS             : self.get_cursor_pos,
            self.PUTCHAR                    : self.putchar,
            self.TELETYPE_PUTCHAR           : self.teletype_putchar,
            self.GET_VIDEO_MODE             : self.get_video_mode,
            self.GET_SHIFT_FLAGS            : self.get_shift_flags,
            self.RESET_DISK                 : self.reset_disk,
            self.READ_SECTORS               : self.read_sectors,
            self.WRITE_SECTORS              : self.write_sectors,
            self.GET_DRIVE_PARAMS           : self.get_drive_params,
            self.CHECK_MEMORY               : self.check_memory,
            self.GET_MEMORY_SIZE            : self.get_memory_size,
            self.QUERY_MEMORY               : self.query_memory,
            self.GET_TIME                   : self.get_time,
            self.SET_TIME                   : self.set_time
        }

    def interrupt(self, intno: int, *args):
        """
        Generate wrappers for interrupts.
        """

        self.interrupt_table[intno](*args)

    def set_video_mode(self, *registers):
        """
        Set the video mode
        Input:
        AH = mode
        AL = submode
        """

        mode = registers[0]

        self.asm.xor(self.regs.AH, self.regs.AH)
        self.asm.mov(self.regs.AL, mode)
        self.asm.int_(0x10)

    def set_cursor_pos(self, *registers):
        """
        Set the cursor position
        Input:
        BH = page
        DH = line
        DL = column
        """

        page = registers[0]
        line = registers[1]
        column = registers[2]

        self.asm.mov(self.regs.AH, 0x02)
        self.asm.mov(self.regs.BH, page)
        self.asm.mov(self.regs.DH, line)
        self.asm.mov(self.regs.DL, column)
        self.asm.int_(0x10)

    def get_cursor_pos(self, *registers):
        """
        Get the cursor position
        Input:
        BH = page

        Output:
        DH = line
        DL = column
        """

        page = registers[0]

        self.asm.mov(self.regs.AH, 0x03)
        self.asm.mov(self.regs.BH, page)
        self.asm.int_(0x10)

    def putchar(self, *registers):
        """
        Write character and attribute at cursor
        Input:
        AL = character
        BL = attribute
        CX = times
        BH = page
        """
        
        char = registers[0]
        attr = registers[1]
        times = registers[2]
        page = registers[3]

        self.asm.mov(self.regs.AH, 0x09)
        self.asm.mov(self.regs.AL, char)
        self.asm.mov(self.regs.BL, attr)
        self.asm.mov(self.regs.CX, times)
        self.asm.mov(self.regs.BH, page)
        self.asm.int_(0x10)

    def teletype_putchar(self, *registers):
        """
        Write character and attribute and advance cursor
        Input:
        AL = character
        BH = page
        BL = attribute
        """

        char = registers[0]
        page = registers[1]
        attr = registers[2]

        self.asm.mov(self.regs.AH, 0x0E)
        self.asm.mov(self.regs.AL, char)
        self.asm.mov(self.regs.BH, page)
        self.asm.mov(self.regs.BL, attr)
        self.asm.int_(0x10)

    def get_video_mode(self, *registers):
        """
        Get current video mode
        Input:
        BH = page

        Output:
        AH = mode
        BL = attribute
        """

        page = registers[0]

        self.asm.mov(self.regs.AH, 0x12)
        self.asm.mov(self.regs.BH, page)
        self.asm.int_(0x10)

    def getchar(self, *registers):
        """
        Get character from the keyboard
        Output:
        AH = scan code
        AL = character ASCII code
        """

        self.asm.xor(self.regs.AH, self.regs.AH)
        self.asm.int_(0x16)

    def getchar2(self, *registers):
        """
        Get character from the keyboard (non-blocking)
        Output:
        ZF = 1 if no character
        AH = scan code
        AL = character ASCII code
        """

        self.asm.mov(self.regs.AH, 0x01)
        self.asm.int_(0x16)

    def get_shift_flags(self, *registers):
        """
        Get shift flags
        Output:
        AL = key modifiers state
        """

        self.asm.mov(self.regs.AH, 0x02)
        self.asm.int_(0x16)

    def reset_disk(self, *registers):
        """
        Reset disk system
        """

        self.asm.xor(self.regs.AH, self.regs.AH)
        self.asm.int_(0x13)

    def read_sectors(self, *registers):
        """
        Read disk sectors (CHS)
        Input:
        AL = number of sectors to read
        CH = cylinder
        CL = sector
        DH = head
        DL = drive number
        ES:BX = buffer

        Output:
        CF = success (0) / error (1)
        """

        nsectors = registers[0]
        cylinder = registers[1]
        sector = registers[2]
        head = registers[3]
        driveno = registers[4]
        bx = registers[5]
        es = registers[6]

        self.asm.push(self.regs.ES)
        self.asm.mov(self.regs.AX, es)
        self.asm.mov(self.regs.ES, self.regs.AX)
        self.asm.mov(self.regs.BX, bx)
        self.asm.mov(self.regs.AH, 0x02)
        self.asm.mov(self.regs.AL, nsectors)
        self.asm.mov(self.regs.CH, cylinder)
        self.asm.mov(self.regs.CL, sector)
        self.asm.mov(self.regs.DH, head)
        self.asm.mov(self.regs.DL, driveno)
        self.asm.int_(0x13)
        self.asm.pop(self.regs.ES)

    def write_sectors(self, *registers):
        """
        Write disk sectors (CHS)
        Input:
        AL = number of sectors to read
        CH = cylinder
        CL = sector
        DH = head
        DL = drive number
        ES:BX = buffer

        Output:
        CF = success (0) / error (1)
        """

        nsectors = registers[0]
        cylinder = registers[1]
        sector = registers[2]
        head = registers[3]
        driveno = registers[4]
        bx = registers[5]
        es = registers[6]

        self.asm.push(self.regs.ES)
        self.asm.mov(self.regs.AX, es)
        self.asm.mov(self.regs.ES, self.regs.AX)
        self.asm.mov(self.regs.BX, bx)
        self.asm.mov(self.regs.AH, 0x03)
        self.asm.mov(self.regs.AL, nsectors)
        self.asm.mov(self.regs.CH, cylinder)
        self.asm.mov(self.regs.CL, sector)
        self.asm.mov(self.regs.DH, head)
        self.asm.mov(self.regs.DL, driveno)
        self.asm.int_(0x13)
        self.asm.pop(self.regs.ES)

    def get_drive_params(self, *registers):
        """
        Get drive parameters
        Input:
        DL = drive number

        Output:
        AH = reader type
        """

        driveno = registers[0]

        self.asm.mov(self.regs.AH, 0x08)
        self.asm.mov(self.regs.DL, driveno)
        self.asm.int_(0x13)

    def check_memory(self, *registers):
        """
        Check memory size/availability
        Input:
        AX = subfunction

        Output:
        CF, AX = error
        """

        subfunc = registers[0]

        self.asm.mov(self.regs.AH, 0x87)
        self.asm.mov(self.regs.AX, subfunc)
        self.asm.int_(0x15)

    def get_memory_size(self, *registers):
        """
        Get memory size
        Output:
        AX = memory size (in KB)
        """

        self.asm.mov(self.regs.AH, 0x88)
        self.asm.int_(0x15)

    def query_memory(self, *registers):
        """
        Query system memory
        Input:
        CX:BX = paragraphs

        Output:
        CF, AX = error
        """

        cx = registers[0]
        bx = registers[0]

        self.asm.mov(self.regs.AH, 0x86)
        self.asm.mov(self.regs.CX, cx)
        self.asm.mov(self.regs.bx, bx)
        self.asm.int_(0x15)

    def get_time(self, *registers):
        """
        Get system time
        Output:
        CX:DX = ticks
        """

        self.asm.xor(self.regs.AH, self.regs.AH)
        self.asm.int_(0x1A)

    def set_time(self, *registers):
        """
        Set system time / RTC
        Input:
        CX:DX = new hour
        """

        cx = registers[0]
        dx = registers[1]

        self.asm.mov(self.regs.AH, 0x02)
        self.asm.mov(self.regs.CX, cx)
        self.asm.mov(self.regs.DX, dx)
        self.asm.int_(0x1A)

    def bootstrap(self, *registers):
        """
        Boot from first drive
        """

        self.asm.int_(0x19)