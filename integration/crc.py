import crcmod

file = open("EthernetDump_5.txt", "r")

file.seek(16,0)
crc32 = crcmod.Crc(0x104c11db7, initCrc=0, xorOut=0xFFFFFFFF)
crc32.update(str(int(file.read(108),16)))
print hex(crc32.crcValue)
print crc32.hexdigest()
'''
crc32 = crcmod.Crc(0x104c11db7, initCrc=0, xorOut=0xFFFFFFFF)
crc32.update('111111111111111111111111111111111111')
print hex(crc32.crcValue)
print crc32.hexdigest()
'''
