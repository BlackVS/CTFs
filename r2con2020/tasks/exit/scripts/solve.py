#!/usr/bin/env python3

import os, sys

d1=bytearray.fromhex("deadbeefdeadbeefcafe1337cafe13370102030405060708090a")
d2=bytearray.fromhex("0a09080706050403020137133713feca37133713fecaefbeadde")

def decode(rx):
    r=bytearray.fromhex(rx)
    res=""
    for i in range(len(r)):
        v = ( r[i] - d2[i])
        v = (v+0x100)%0x100
        #print("{:02x} - {:02x} = {:02x}".format(r[i], d2[i], v))
        v ^= d1[i]
        v = (v+0x100)%0x100
        #print("v ^ {:02x} = {:02x}".format(d1[i], v))
        res+=chr(v)
    print(res)


decode("97cdd2d6c0c7cd84ec91ad62f5f165225882b137613e5d2b144c")
decode("9ccde18eb092d791c09eb2")
decode("97e2e79d")