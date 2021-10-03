# Task 7

![text](img/desc.png)

## Input file:

[capture.pcapng](input/capture.pcapng)

## Solution:

The task the same same as in 
[HWIO2021 CTS, Task 7](https://github.com/BlackVS/CTFs/blob/master/HWIO2021/CTS/task7.md)

I was right in general solution approach and some assumptions made at the end of mentioned write-up but


## 1. USB data parsing

Just to extract using:
```bash
"C:\Program Files\Wireshark\tshark.exe" -r data.pcapng -T fields -e usb.capdata -Y usb.capdata > capdata.raw
```
was not correct way.

If look more carefully to packets flow we will see that each write operation consist of 2 steps:

![shark0](img/wshark00.png)

- send address to be written to (LBA - Logical Bloak Address)
- send data

Filter only this packets and check them

![shark0](img/wshark01.png)

We see that packets not written sequentially - sometimes other blocka written and it is normal due to it is USB drive which is random access device.

To extract data more accuratly we need check LBA addresses and sort written data in LBA order.

I.e. to extract raw USB data I did:

1. Filter specific packets (image above)
2. Exported them to the old fromat .pcap (I didn't exported to .pcapng due to need only raw packets processing in my Python script
3. Extracted ordered raw data using my Python [script](sricpts/parse.py):
```python
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
```

Offsets like "0x51:0x55" I got inspecting packets in Wireshark

4. Now we have **usbtraffic.raw** file which I analyzed using binwalk with -e option.
Surprise - extracted data much larger comparing to the extrected in my write-p from HWIO2021 %)


## 2. Demodulating

My suggestion [HWIO2021 CTS, Task 7](https://github.com/BlackVS/CTFs/blob/master/HWIO2021/CTS/task7.md) in was correct - it is GSM signal.

But why grgsm_decode decoded nothing?

Reson is quite ... silly? Thanks to Don (flamewires team) who pushed me in right direction.

Opening signal using default GNURadio 
