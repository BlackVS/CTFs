#!/usr/bin/env python3
import os,sys
from itertools import *
coded = [ 0x60, 0x70, 0x54, 0x51, 0x65, 0x70, 0x51, 0x60, 0x65, 0x54, 0x51, 0x60, 0x50, 0x54, 0x65, 0x60, 0x71, 0x54, 0x50, 0x60 ]

cand = ""
idx = 1
s = 1
for i in range(20):
    res=""
    for c in range(97,123):
        if ((c^0x28)+0x15)&0xf5 == coded[i]:
            res+=chr(c)
    print("{:2}: {:4} {}".format(i,res, " ".join( map(lambda c: hex(ord(c)), res ) ) ))
    cand+=res[idx]
    idx ^= 1
    s*=len(res)

print("The first good candidate is: {}".format(cand))

print("Amount of variants is: {}".format(s))