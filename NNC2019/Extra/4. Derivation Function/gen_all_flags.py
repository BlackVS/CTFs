#!/usr/bin/env python3

import os, sys
import argparse
import hashlib
import binascii
flags = [ ("#1 Mr Bean Walker", "flag{wELcOMe_mR_8E4n_w4LKER}" ),
          ("#5 Binary Hero",    "flag{bfd251b9d253ab0aea83554efb8d}") ]

codepharses = [ ("#2 BruteSearcher", "BruteSearcher"),
                ("#3 NoNameCon SpyNet", "NoNameCon SpyNet"),
                ("#4 Ployka PWNer", "Ployka PWNer"),
                ("#6 Side Blennel", "Side Blennel") ]


def main():

    parser = argparse.ArgumentParser(add_help=True, description='ESP32 analyzer')

    parser.add_argument('--deviceid', '-d',
                        help='Target badge deviceID',
                        default=None)
    
    parser.add_argument('--mac', '-m',
                        help='Target badge base mac ( esptool read_mac )',
                        default=None)

    args = parser.parse_args()

    if not args.deviceid and not args.mac:
        print("Wrong arguments!!!")
        parser.print_help()
        exit(0)

    devid = ""
    if args.mac:
        mac = args.mac.split(":")
        if len(mac)!=6:
            print("Wrong mac!!!")
            exit(1)
        macs  = [int(m,base=16) for m in mac ]
        macsb = bytearray(macs)
        
        print("MAC: {}".format( macsb.hex()))
        devid = hashlib.sha256(macsb).digest()[:6]
        devidhex = hashlib.sha256(macsb).hexdigest()[:12]
    
    if args.deviceid:
         devidhex = args.deviceid.strip()
         devid = bytes.fromhex(devidhex)
    
    print("Device ID: {}".format(devidhex) )

    for i, (cname, ccode) in enumerate(codepharses):
        cin = devid + ccode.encode()[6:]
        flag = hashlib.sha256(cin).hexdigest()[:28]

        #print("flag({})".format(flag))
        flags.append( (cname, "flag{{{}}}".format(flag) ) ) 

    print("+--------------------+---------------------------------------+")
    print("| Challenge          | Flag                                  |")
    print("+--------------------+---------------------------------------+")
    for chname, flag in sorted(flags):
        print("| {:19}| {:37} |".format(chname, flag))
    print("+--------------------+---------------------------------------+")


def _main():
    try:
        main()
    except Exception as inst:
        print(type(inst))
        print(inst.args)
        print(inst)



if __name__ == '__main__':
    _main()
