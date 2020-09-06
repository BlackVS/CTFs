#/usr/bin/python3
import sys

sys.path.append('..')
import esptool, espefuse
import argparse
from binascii import *

def hexify(bitstring, separator=""):
    try:
        as_bytes = tuple(ord(b) for b in bitstring)
    except TypeError:  # python 3, items in bitstring already ints
        as_bytes = tuple(b for b in bitstring)
    return separator.join(("%02x" % b) for b in as_bytes)


def log(f, txt=""):
    print(txt)
    f.write( "{}\n".format(txt))

def image_info(chip,filename):
    f_info=open("{}.info".format(filename),"wt+")
    f_map =open("{}.map".format(filename),"wt+")

    image = esptool.LoadFirmwareImage(chip, filename)
    log(f_info, "Image version: {}".format( image.version ) )
    if image.entrypoint != 0:
        log(f_info, "Entry point: {:08x}".format(image.entrypoint))
    else:
        log(f_info, "Entry point not set")
    log(f_info, "secure_pad: {}".format(image.secure_pad))
    log(f_info, "flash_mode: {}".format(image.flash_mode))
    log(f_info, "flash_size_freq: {}".format(image.flash_size_freq))
    f_map.write("0x{:x}\n".format(image.entrypoint))
    f_map.write("{}\n".format(len(image.segments)))
    f_map.write("{} {} {} \n".format(image.secure_pad,image.flash_mode,image.flash_size_freq))

    log(f_info, '%d segments' % len(image.segments))
    log(f_info)

    idx = 0
    for seg in image.segments:
        idx += 1
        log(f_info, "Segment {}: {}".format( idx, seg))
        log(f_info, "  addr=0x{:x} file_offs=0x{:x} include_in_checksum={}\n".format(seg.addr, seg.file_offs, seg.include_in_checksum))
        fsegname="{}.seg{}".format(filename,idx)
        with open(fsegname, "wb+") as file:
            file.write(seg.data)
        f_map.write("{} {} 0x{:x} 0x{:x} {}\n".format(idx, fsegname, seg.addr, seg.file_offs, seg.include_in_checksum))

            
    calc_checksum = image.calculate_checksum()
    log(f_info, 'Checksum: %02x (%s)' % (image.checksum, 'valid' if image.checksum == calc_checksum else 'invalid - calculated %02x' % calc_checksum))
    try:
        digest_msg = 'Not appended'
        if image.append_digest:
            is_valid = image.stored_digest == image.calc_digest
            digest_msg = "%s (%s)" % (hexify(image.calc_digest).lower(),
                                      "valid" if is_valid else "invalid")
            print('Validation Hash: %s' % digest_msg)
    except AttributeError:
        pass  # ESP8266 image has no append_digest field

    f_map.close()
    f_info.close()
    print("END")


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(add_help=True, description='ELF bin disasemble')
        parser.add_argument("input_file", help="input bin file to disassemble")
        if len(sys.argv) == 1:
            print("Wrong arguments!!!")
            parser.print_help()
            exit(0)
        args = parser.parse_args()
        image_info("esp32", args.input_file)
    except Exception as inst:
        print(type(inst))
        print(inst.args)
        print(inst)


