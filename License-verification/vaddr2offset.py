#!/usr/bin/env python3
# vaddr2offset.py
# Usage: ./vaddr2offset.py <elf-file> <vaddr-hex>
# Example: ./vaddr2offset.py verifier 0x4011a2
# Output: file offset as hex
import sys
import struct

def usage():
    print("Usage: {} <elf-file> <vaddr-hex>".format(sys.argv[0]))
    sys.exit(2)

if len(sys.argv) != 3:
    usage()

elf = sys.argv[1]
vaddr = int(sys.argv[2], 0)

with open(elf, "rb") as f:
    data = f.read()

# Check ELF class (32/64)
if data[0:4] != b'\x7fELF':
    print("Not an ELF file")
    sys.exit(1)

ei_class = data[4]
if ei_class == 1:
    is64 = False
elif ei_class == 2:
    is64 = True
else:
    print("Unknown ELF class")
    sys.exit(1)

# parse program headers
if is64:
    e_phoff = struct.unpack_from("<Q", data, 32)[0]
    e_phentsize = struct.unpack_from("<H", data, 54)[0]
    e_phnum = struct.unpack_from("<H", data, 56)[0]
    fmt = "<IIQQQQQQ"
else:
    e_phoff = struct.unpack_from("<I", data, 28)[0]
    e_phentsize = struct.unpack_from("<H", data, 42)[0]
    e_phnum = struct.unpack_from("<H", data, 44)[0]
    fmt = "<IIIIIIII"

for i in range(e_phnum):
    off = e_phoff + i * e_phentsize
    if is64:
        (p_type, p_flags, p_offset, p_vaddr, p_paddr, p_filesz, p_memsz, p_align) = struct.unpack_from("<IIQQQQQQ", data, off)
    else:
        (p_type, p_offset, p_vaddr, p_paddr, p_filesz, p_memsz, p_flags, p_align) = struct.unpack_from("<IIIIIIII", data, off)
    # PT_LOAD == 1
    if p_type != 1:
        continue
    if vaddr >= p_vaddr and vaddr < (p_vaddr + p_memsz):
        file_offset = p_offset + (vaddr - p_vaddr)
        print(hex(file_offset))
        sys.exit(0)

print("Address not within any PT_LOAD segment")
sys.exit(1)
