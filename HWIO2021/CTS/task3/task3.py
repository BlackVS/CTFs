#!/usr/bin/env python3

signal = "10111010001100101001001000101010100010011101000110001001101010010111000110010001101000100011101001000011110100010110001010011010110010100111001000011001110100011000001111000001101010100001101010101010101011010011100000000"
for shift in range(8):
    bits=signal[shift:]
    shifted = [ int("".join(map(str,bits[i:i+8])),2) for i in range(0,len(bits),8)]
    temp="".join(map(chr,shifted))
    print(temp.encode())

# https://www.digital.security/en/blog/hardweario-capture-signal-write
# b'FREQ:15.24GHz,SYNC:0x5CUU\xc2\xa7'