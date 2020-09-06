#!/usr/bin/env python3
import os, sys

SBox = None
SBoxInv = None
Sbox_fpos = 0x1b40



Tboxes0 = None
TBoxes0_fpos = 0x86020

buf = None
with open("whitebox", "rb") as f:
    buf = f.read()

shifttab = [0, 5, 10, 15, 4, 9, 14, 3, 8, 13, 2, 7, 12, 1, 6, 11]
shifttab_rev = [0] *16
for i in range(16):
    shifttab_rev[ shifttab[i] ] = i

SBox = [0]*256
for i in range(256):
    SBox[i] = buf[Sbox_fpos+i]

Tboxes0 = [[0]*256 for _ in range(16)]
for i in range(16):
    for j in range(256):
       Tboxes0[i][j]=buf[TBoxes0_fpos+i*256+j]

#for i in range(0,256,16):
#    print(" ".join(map(lambda v: "{:02x}".format(v), SBox[i:i+16])))

SBoxInv = [0]*256
for i in range(256):
    sb=SBox[i]
    SBoxInv[sb]=i

#print()
#for i in range(0,256,16):
#    print(" ".join(map(lambda v: "{:02x}".format(v), SBoxInv[i:i+16])))


#print()
#for j in range(16):
#    print("j={}".format(j))
#    for x in range(0,256,16):
#        print(" ".join(map(lambda v: "{:02x}".format(v), Tboxes0[j][x:x+16])))


#for x in range(256):
x=0
r=""
rt=""
for j in range(16):
    c  = Tboxes0[j][x]
    ci = SBoxInv[c]
    r+="{:02x}".format(ci^x)
    rt+=chr(ci^x)
print("Extended key: {}".format(rt))

res=""
for i in range(16):
    res+=rt[shifttab_rev[i]]
print("Flag is r2con{{{}}}".format(res))
