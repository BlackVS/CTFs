#!/usr/bin/env python3
import os,sys
from itertools import *
coded = [ 0x60, 0x70, 0x54, 0x51, 0x65, 0x70, 0x51, 0x60, 0x65, 0x54, 0x51, 0x60, 0x50, 0x54, 0x65, 0x60, 0x71, 0x54, 0x50, 0x60 ]

cand = ""
idx = 1
for i in range(20):
    res=""
    for c in range(97,123):
        if ((c^0x28)+0x15)&0xf5 == coded[i]:
            res+=chr(c)
    print("{:2}: {:4} {}".format(i,res, " ".join( map(lambda c: hex(ord(c)), res ) ) ))
    cand+=res[idx]
    idx ^= 1
print(cand)


#for p in product( 'prxz', 'su', 'ln', 'ce', 'prxz', 'aio', 'ln', 'ce', 'km', 'aio', 'prxz', 'ce', 'tv', 'aio', 'km', 'ce' ):
#for p in product( 'ce', 'prxz', 'aio', 'ln', 'ce', 'km', 'aio', 'prxz', 'ce', ['take','time','tome']):
for p in product( 'prxz', 'su', 'ln', 'ce', 'prxz', 'aio', 'ln', 'ce', ['more'], ['time']):
    print("esil"+"".join(p))


esilrulezonemoretime