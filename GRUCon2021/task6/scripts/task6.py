#!/usr/bin/env python3

import os, sys

smap = {
    '00': '0',
    '01': '1',
    '10': '2'
}

fo = open("out.txt","wt+")
res = ""

with open("bits.txt","rt") as f:
    lines=f.readlines()
    txt = lines[0]
    print(txt)
    for i in range( 0, len(txt), 8):
        #print(smap[txt[i:i+2]])
        #print(txt[i:i+8][:2])
        c = smap[txt[i:i+8][:2]]
        fo.write(c)
        res+=c
fo.close()





