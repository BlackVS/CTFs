#!/usr/bin/python
import binascii
import dpkt
import struct
import sys

# Start the pcap file parsing
f = open("usbtraffic.pcap", 'rb')
pcap = dpkt.pcap.Reader(f)
#print(pcap)
lba = 0
packets = []
for ts, buf in pcap:
    #print(ts)
    if buf[64:68] == b'USBC':
        #lba = int( buf[], 16)
        a = buf[0x51:0x55]
        lba = int.from_bytes(a, 'big')
        b = buf[0x56:0x58]
        blen = int.from_bytes(b, 'big')
        print(hex(lba))
    else:
        packets.append(  (lba, blen, ts, buf[64:] ) )

packets.sort()
with open("usbtraffic.raw","wb+") as f:
    for lba, blen, ts, b in packets:
        print("Writing lba={} len={} ts={}".format(lba, blen, ts))
        f.write(b)
