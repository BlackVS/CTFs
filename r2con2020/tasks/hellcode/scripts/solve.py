#!/usr/bin/env python3

import os, sys

base ="binary"

text = ""
for i in range(111):
    fname = "{}{}".format(base, i)
    with open(fname, "rb") as f:
        buf = f.read()
        a, b = buf[0x10bc], buf[0x10d6]
        if buf[0x10ba]==0x80 and buf[0x10bb]==0xea: #sub
            c = a+b
        elif buf[0x10ba]==0x80 and buf[0x10bb]==0xf2: #xor
            c = a^b
        elif buf[0x10ba]==0x80 and buf[0x10bb]==0xc2: #add 
            c = b-a
        else:
            assert(0)
        print("{:3}: {:02x} {:02x} = {:02x} {} ".format(i,a,b,c%256,chr(c%256)))
        text+=chr(c%256)

print(text)