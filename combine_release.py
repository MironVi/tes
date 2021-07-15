#!/bin/python3

from crccheck.crc import Crc16CcittFalse
import os
import crc16

SOFTWARE_FILE = "net_gateway.bin"
OUTPUT_FILE = "net_gateway.bin1"

#SOFTWARE_POSITION = 0x5000
#FILE_SIZE = (1024 * 512)

#, open(OUTPUT_FILE, "wb") as output

with open(SOFTWARE_FILE, "rb") as software , open(OUTPUT_FILE, "wb") as output:
    #output.write(boot_data)
    #output.write(bytearray(0xff for i in range(SOFTWARE_POSITION - len(boot_data) - 6)))
    software_data = software.read()
    #output.write(bytearray(len(software_data).to_bytes(4, "little")))
    crc = Crc16CcittFalse()
    crc.process(software_data)
    output.write(bytearray(crc.finalbytes("little")))
    output.write(software_data)

    print(f"Size of application: {len(software_data)}")
    print(f"Crc of application: {crc.finalhex()}")
    #print(crc16(software.read()))
    #print(f"Size of application with bootloader: {len(software_data) + SOFTWARE_POSITION}")
    #print(f"Path to created bin: {os.path.abspath(OUTPUT_FILE)}")
    # output.write(bytearray(0xff for i in range(FILE_SIZE - SOFTWARE_POSITION - len(software_data))))
