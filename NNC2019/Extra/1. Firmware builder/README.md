# Badge Firmware builder

ESP32 allows both [secure boot and flash encryption](https://docs.espressif.com/projects/esp-idf/en/latest/security/secure-boot.html#secure-boot-and-flash-encr) but NoNameBadge uses only the first one - i.e. unencrypted but signed flash image. 

The structure of image is quite simple - https://github.com/espressif/esptool/wiki/Firmware-Image-Format

I.e. actually we have two levels of protection:

- simple, checksum (is defined as the xor-sum of all bytes and the byte 0xEF)
- complex, signing

After solving **Ployka PWNer** you already have needed private key for signing %)
Here is few simple scripts for reassembling badge image and signing it.

## 1. Image disassembly

Image can be patched inplace and re-signed but it is more convinient to extract all segments, open and patch needed segment using some tools (I used radare2) and assemble, sign.
I made *nnc_assemble.py* Python 3 script to do this job (check *Extra\1. Firmware builder\\scripts\\* folder ).
To use it you need *Python3* and *argparse*, *esptool* modules installed:

```bash
pip install argparse
pip install esptool
```

To disaasemble (not to be confused with dissassembling using disassembler):

```bash
nnc_disassemble.py nn-badge195.bin 
```

As result a set of files nn-badge195.bin.* will be produced:
*nn-badge195.bin.info* - human-friendly file info, also printed on console;
*nn-badge195.bin.map* - file map, similar to file info but in compact, machine-friendly form (used by *nnc_assemble.py* script) );
We same info can be get via

```bash
esptool.py --chip esp32 image_info nn-badge195.bin
```

*nn-badge195.bin.segN* - raw dump of each segment (in our case it consists of 6 segments).
I.e. running 

```bash
nnc_disassemble.py nn-badge195.bin 
```

you should see something similar to:
```bash
Image version: 1
Entry point: 40080ffc
secure_pad: False
flash_mode: 2
flash_size_freq: 32
6 segments

Segment 1: len 0x2bcb0 load 0x3f400020 file_offs 0x00000018
  addr=0x3f400020 file_offs=0x18 include_in_checksum=True

Segment 2: len 0x03614 load 0x3ffbdb60 file_offs 0x0002bcd0
  addr=0x3ffbdb60 file_offs=0x2bcd0 include_in_checksum=True

Segment 3: len 0x00400 load 0x40080000 file_offs 0x0002f2ec
  addr=0x40080000 file_offs=0x2f2ec include_in_checksum=True

Segment 4: len 0x00914 load 0x40080400 file_offs 0x0002f6f4
  addr=0x40080400 file_offs=0x2f6f4 include_in_checksum=True

Segment 5: len 0xd1f18 load 0x400d0018 file_offs 0x00030010
  addr=0x400d0018 file_offs=0x30010 include_in_checksum=True

Segment 6: len 0x15b64 load 0x40080d14 file_offs 0x00101f30
  addr=0x40080d14 file_offs=0x101f30 include_in_checksum=True

Checksum: 33 (valid)
Validation Hash: 94f0a1f483bf3b0db3ec20f26bf4f7dab910487b228b6d4885bfdf79562074f5 (valid)
END
```

and map file should look like (if you analyze 1.95 image file):

```bash
0x40080ffc
6
False 2 32 
1 nn-badge195.bin.seg1 0x3f400020 0x18 True
2 nn-badge195.bin.seg2 0x3ffbdb60 0x2bcd0 True
3 nn-badge195.bin.seg3 0x40080000 0x2f2ec True
4 nn-badge195.bin.seg4 0x40080400 0x2f6f4 True
5 nn-badge195.bin.seg5 0x400d0018 0x30010 True
6 nn-badge195.bin.seg6 0x40080d14 0x101f30 True
```

Some useful information can be seen in debug info during badge reboot:

```bash
I (63) boot:  0 nvs              WiFi data        01 02 00009000 00004000
I (70) boot:  1 otadata          OTA data         01 00 0000d000 00002000
I (78) boot:  2 phy_init         RF data          01 01 0000f000 00001000
I (85) boot:  3 ota_0            OTA app          00 10 00010000 00180000
I (93) boot:  4 ota_1            OTA app          00 11 00190000 00180000
I (100) boot:  5 nvs_key          NVS keys         01 04 00310000 00001000
```

Our firmware image is ... ota_1. Why? ota_0 - is factory image. I.e. it is badge life preserver if custom image (ota_1) is broken %)
You can read in details about boot process [here](https://docs.espressif.com/projects/esp-idf/en/latest/api-guides/bootloader.html)

## 2. Patching

To get all flags we need patch badge code. 
After *Binary Hero* task we already know - we have to patch *nn-badge195.bin.seg5* (flag generating function are in this segment address space).
To do this you may load it to *radare2* mapping to address *0x400d0018* and patch (but as it will be shown in the second article it is not so easy task as could be expected)

## 3. Assemble image

I patched in-place without changing segments sizes.
It allows assemble all segments very easy using the same map file *nn-badge195.bin.map*:

```bash
nnc_assemble.py nn-badge195.bin.map nn-test.bin
```

If you change segments sizes you need update accordingly map file.

## 4. Signing

```bash
espsecure.py sign_data -k private.pem nn-test.bin
```

output is:
```bash
espsecure.py v2.6
Signed 1145536 bytes of data from nn-test.bin with key private.pem
```
## 5. Verifying

```bash
espsecure.py verify_signature -k public.key nn-test.bin
```
->
```bash
espsecure.py v2.6
Verifying 1145536 bytes of data
Signature is valid
```
**Signature must be valid!**

and check image info of patched file:

```bash
esptool.py --chip esp32 image_info nn-test.bin
```
->
```bash
esptool.py v2.6
Image version: 1
Entry point: 40080ffc
6 segments
Segment 1: len 0x2bcb0 load 0x3f400020 file_offs 0x00000018
Segment 2: len 0x03614 load 0x3ffbdb60 file_offs 0x0002bcd0
Segment 3: len 0x00400 load 0x40080000 file_offs 0x0002f2ec
Segment 4: len 0x00914 load 0x40080400 file_offs 0x0002f6f4
Segment 5: len 0xd1f18 load 0x400d0018 file_offs 0x00030010
Segment 6: len 0x15b64 load 0x40080d14 file_offs 0x00101f30
Checksum: 33 (valid)
Validation Hash: 94f0a1f483bf3b0db3ec20f26bf4f7dab910487b228b6d4885bfdf79562074f5 (valid)
```

**You must have both checksum and validation hash valid!!!**

## 6. Flashing

```bash
esptool.py -p com4 -c esp32 write_flash 0x190000 nn-test.bin
```
(you may have different from my com port).

As you see we flashing *ota_1* .


## Useful links

* https://www.espressif.com/en/support/download/documents
* https://docs.espressif.com/projects/esp-idf/en/latest/security/secure-boot.html
* https://github.com/espressif/esptool/wiki/Firmware-Image-Format
* https://docs.espressif.com/projects/esp-idf/en/latest/api-guides/partition-tables.html
* https://github.com/espressif/esptool
* http://cholla.mmto.org/esp8266/xtensa.html
* https://medium.com/@tomac/turning-a-10-esp32-into-a-hacker-arsenals-winx-portable-clone-46c37c1508cd
 
## Useful commands

```bash
esptool.py --chip esp32 --port com4 chip_id
esptool.py --chip esp32 --port com4 read_flash 0x9000 0x4000 nvs.flash
esptool.py --chip esp32 --port com4 read_flash 0x190000 0x00180000 ota1.flash
```
