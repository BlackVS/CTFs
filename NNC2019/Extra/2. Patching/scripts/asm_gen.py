#!/usr/bin/env python
import sys
import argparse
from binascii import *


def rshift(val,n):
    mask1 = 0x80000000
    sign = (val & mask1)
    mask3 = (~((1<<(32-n))-1), 0)[sign==0] #python support big numbers
    return (val>>n) | mask3

#The target instruction
#address of the call is given by the address of the CALL8 instruction with the two
#least significant bits set to zero, plus the sign-extended 18-bit offset field of the instruction
#shifted by two, plus four.
def make_call8(pc,offset):
    start=pc&~0b11
    if offset&0b11:
        print("Offset must have 2 lowest bits equal to zero i.e. 4 bytes aligned")
        return
    # offset = pc + (diff<<<2) + 4 => 
    diff= ( offset - start - 4 ) 
    # instraction = offset (18bit) + 10 + 0101
    byte0 = 0b100101 |( ( diff & 0b1100 )<<4)
    byte1 = (diff & 0b111111110000) >> 4
    byte2 = (diff & 0b11111111000000000000) >> 12
    print("{:08x}: call8 {:08x} = {:02x} {:02x} {:02x}".format(pc, offset, byte0, byte1, byte2))
    return pc+3

#L32R forms a virtual address by adding the 16-bit one-extended constant value encoded
#in the instruction word shifted left by two to the address of the L32R plus three with the
#two least significant bits cleared. Therefore, the offset can always specify 32-bit aligned
#addresses from -262141 to -4 bytes from the address of the L32R instruction. 32 bits
#(four bytes) are read from the physical address. This data is then written to address
#register at.
#  offset = (0b11111111 | imm16) << 2 + 
#  start = ( (pc + 3) & ~0b11 )
#  offset = (0b11111111 | imm16) << 2 + start
#  imm16 = ( (offset - start) >>> 2 ) & 0b11111111

#   where >>> is argipmhetic shift, rshift

def make_l32r(pc,regNum,offset):
    start = (pc+3) & ~0b11
    byte0 = 0b0001 | ( regNum << 4 )
    imm16 = rshift( offset - start, 2 )
    byte1 = imm16 & 0xff
    byte2 = (imm16>>8) & 0xff
    print("{:08x}: l32r a{}, {:08x} = {:02x} {:02x} {:02x}".format(pc, regNum, offset, byte0, byte1, byte2)) #LE
    return pc+3



#|           0x400d5488      366100                 entry a1, 48
#|           0x400d548b      call8 fcn.400d51bc ; fcn.400d51ba+0x2
#                            call8 printf ; 0x400d689c
#                            l32r a10, 0x400d0444
#                            call8 gen_flag
#                            call8 printf ; 0x400d689c
#                            l32r a10, 0x400d044c
#                            call8 gen_flag
#                            call8 printf ; 0x400d689c
#                            l32r a10, 0x400d0454
#                            call8 gen_flag
#                            call8 printf ; 0x400d689c
#                            l32r a10, 0x400d0460
#                            call8 gen_flag
#                            call8 printf ; 0x400d689c
#                            l32r a10, 0x400d043c
#                            call8 printf ; 0x400d689c


if __name__ == '__main__':
    #0x400d5494      a1eceb                 l32r a10, 0x400d0444
    #pc=0x400d5494
    #pc=make_l32r(pc, 10, 0x400d0444) # => a1 ec eb

    pc=0x400d548b
    pc=make_call8(pc, 0x400d51bc) #hidden flag
    pc=make_call8(pc, 0x400d689c) #printf
    pc=make_l32r(pc, 10, 0x400d0444) #l32r a10, 0x400d0444
    pc=make_call8(pc, 0x400d5108) #gen_flag
    pc=make_call8(pc, 0x400d689c) #printf
    pc=make_l32r(pc,  10, 0x400d044c) #l32r a10, 0x400d044c
    pc=make_call8(pc, 0x400d5108) #gen_flag
    pc=make_call8(pc, 0x400d689c) #printf
    pc=make_l32r(pc,  10, 0x400d0454) #l32r a10, 0x400d0454
    pc=make_call8(pc, 0x400d5108) #gen_flag
    pc=make_call8(pc, 0x400d689c) #printf
    pc=make_l32r(pc,  10, 0x400d0460) #l32r a10, 0x400d0460
    pc=make_call8(pc, 0x400d5108) #gen_flag
    pc=make_call8(pc, 0x400d689c) #printf
    pc=make_l32r(pc,  10, 0x400d043c) #Welcome flag
    pc=make_call8(pc, 0x400d689c) #printf

