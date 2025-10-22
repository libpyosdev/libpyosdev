# 8086 support
---
This is a detailed section about the 8086 support and not a tutorial.

## Summary
- [Informations](#informations)
- [Registers](#registers)
- [Instructions](#instructions)
- [BIOS](#bios)

## Informations
- **16-bit** architecture
- Max memory: 1MB

## Registers
All the 8086 registers are stored in the `Registers8086` class.

### Flags
- CF
- PF
- AF
- ZF
- SF
- TF
- IF
- DF
- OF

### 8-bit registers
- AH
- AL
- BH
- BL
- CH
- CL
- DH
- DL

### 16-bit registers
- AX
- BX
- CX
- DX
- SP
- BP
- SI
- DI
- FLAGS
- IP

### Segment registers
- CS
- DS
- ES
- SS

## Instructions
All the 8086 instructions are stored into the `Instr8086` class.

### General instructions
- mov
- xchg
- lea
- lds
- les
- lahf
- sahf
- push
- pop
- pushf
- popf
- add
- adc
- sub
- sbb
- mul
- imul (2 forms)
- div
- idiv
- neg
- cmp
- not
- and
- or
- xor
- test
- shl
- sal
- shr
- sar
- rol
- ror
- rcl
- rcr
- jmp
- call
- ret (2 forms)
- je
- jz
- jne
- jnz
- jl
- jle
- jg
- jge
- jnle
- jnge
- jng
- jc
- jnc
- jo
- jno
- js
- jns
- loop
- loope
- loopz
- loopne
- loopnz
- jcxz
- movsb
- movsw
- lodsb
- lodsw
- stosb
- stosw
- scasb
- scasw
- cmpsb
- cmpsw
- clc
- stc
- cli
- sti
- cld
- std
- nop
- hlt
- wait
- esc
- int
- int3
- iret

### Assembly directives and symbols
- CURRENT_ADDRESS
- SEGMENT_START
- comment
- org
- db
- dw
- resb
- resw

## BIOS
The 8086 BIOS is represented by the `BIOS_8086` class.

### Interrupts
| Constants         | Input registers (in order) |
| ------------------|----------------------------|
| SET_VIDEO_MODE    | AL
| SET_CURSOR_POS    | BH, DH, DL
| GET_CURSOR_POS    | BH
| PUTCHAR           | AL, BL, CX, BH
| TELETYPE_PUTCHAR  | AL, BH, BL
| GET_VIDEO_MODE    | BH
| GETCHAR           | -
| GETCHAR2          | -
| GET_SHIFT_FLAGS   | -
| RESET_DISK        | -
| READ_SECTORS      | AL, CH, CL, DH, DL, BX, ES
| WRITE_SECTORS     | AL, CH, CL, DH, DL, BX, ES
| GET_DRIVE_PARAMS  | DL
| CHECK_MEMORY      | AX
| GET_MEMORY_SIZE   | -
| QUERY_MEMORY      | CX, BX
| GET_TIME          | -
| SET_TIME          | CX, DX