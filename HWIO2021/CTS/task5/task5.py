#!/usr/bin/env python3

signal =  "1111001001010011010010110011101110011011000010111011101010011011010010110010001101001011011100110011101010010011001010110011001101001011011000110110001010110011010010111001101100011011011110111001101101001011101000111100101000101010011110100011"

for shift in range(8):
    bits=signal[shift:]
    shifted = [ int("".join(map(str,bits[i:i+8])),2) for i in range(0,len(bits),8)]
    temp="".join(map(chr,shifted))
    print(temp.encode())

# b'JigsawSidingRefillViscosityEO#'