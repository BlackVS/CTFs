#!/usr/bin/env python3

signal =  "00000000000011100100011001001100010000010100011100111010010100110101100101001110010000110011101000110000011110000100011001000001"

for shift in range(8):
    bits=signal[shift:]
    shifted = [ int("".join(map(str,bits[i:i+8])),2) for i in range(0,len(bits),8)]
    temp="".join(map(chr,shifted))
    print(temp.encode())
