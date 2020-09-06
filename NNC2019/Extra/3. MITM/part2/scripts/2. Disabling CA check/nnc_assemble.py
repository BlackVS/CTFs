#!/usr/bin/env python
import sys
import argparse
import esptool, espefuse
from binascii import *

def hexify(bitstring, separator=""):
    try:
        as_bytes = tuple(ord(b) for b in bitstring)
    except TypeError:  # python 3, items in bitstring already ints
        as_bytes = tuple(b for b in bitstring)
    return separator.join(("%02x" % b) for b in as_bytes)


def image_assemble(map_file, bin_file):

    image = esptool.ESP32FirmwareImage()

#    for (seg, addr) in zip(args.segfile, args.segaddr):
#        with open(seg, 'rb') as f:
#            data = f.read()
#            image.segments.append(ImageSegment(addr, data))
#    image.entrypoint = args.entrypoint
#    image.save(args.output)

    with open(map_file,"rt") as finfo:
        p_entrypoint   = int(finfo.readline(), 0)
        print("Entrypoint: {:08x}".format(p_entrypoint))
        image.entrypoint = p_entrypoint

        p_segments_num = int(finfo.readline(), 0)
        print("The number of segments: {}".format(p_segments_num))

        s1,s2,s3,_ = finfo.readline().split(" ")
        p_secure_pad = s1=="True"
        p_flash_mode = int(s2)
        p_flash_size_freq = int(s3)
        image.secure_pad = p_secure_pad
        image.flash_mode = p_flash_mode
        image.flash_size_freq = p_flash_size_freq

        for i in range(p_segments_num):
            s1,s2,s3,s4,s5 = finfo.readline().split(" ")
            seg_idx = int(s1)
            seg_fname = s2
            seg_load_address = int(s3,0)
            seg_file_offset  = int(s4,0)
            seg_in_checksum  = s5.startswith("True")
            print("{}: file={} map={:08x} file_ofs={:08x} in_checksum={}".format(seg_idx, seg_fname, seg_load_address, seg_file_offset, seg_in_checksum))
            with open(seg_fname, 'rb') as f:
                data = f.read()
                image.segments.append(esptool.ImageSegment(seg_load_address, data))            
    image.save(bin_file)

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(add_help=True, description='ELF bin disasemble')
        parser.add_argument("input_map_file",  help="input map file")
        parser.add_argument("output_bin_file", help="output bin file")
        if len(sys.argv) == 1:
            print("Wrong arguments!!!")
            parser.print_help()
            exit(0)
        args = parser.parse_args()
        image_assemble(args.input_map_file, args.output_bin_file)
    except Exception as inst:
        print(type(inst))
        print(inst.args)
        print(inst)

