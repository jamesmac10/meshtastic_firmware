#!/usr/bin/env python2

# This is a layout for 4MB of flash
# Name,   Type, SubType, Offset,  Size, Flags
# nvs,      data, nvs,     0x9000,  0x6000,
# otadata,  data, ota,     , 0x2000,
# app0,     app,  ota_0,   , 0x1c0000,
# app1,     app,  ota_1,   , 0x1c0000,
# spiffs,   data, spiffs,  , 0x06f000,

start = 0x9000
nvssys = 0x3000
nvsuser = 0x2000 # NOTE: ti seems total size of nvssys MUST be 0x5000 or device will bootloop
nvs = nvssys + nvsuser
ota = 0x2000
# app = 0x1c0000
spi = 128 * 1024

# treat sys part sizes + spiffs size as reserved, then calculate what appsize can be
reserved = start + nvs + ota + spi
maxsize = 0x400000 # 4MB

app = (maxsize - reserved) / 2

# total = start + nvs + ota + 2 * app + spi

nvskb = nvsuser / 1024
spikb = spi / 1024
appkb = app / 1024

table = """
# This is autogenerated by genpartions.py - change that tool instead!
# appsize={appkb} KB, spiffs={spikb} KB, usernvs={nvskb} KB
# Name,   Type, SubType, Offset,  Size, Flags
nvs,      data, nvs,     0x{start:x},  0x{nvs:x},
otadata,  data, ota,     , 0x{ota:x},
app0,     app,  ota_0,   , 0x{app:x},
app1,     app,  ota_1,   , 0x{app:x},
spiffs,   data, spiffs,  , 0x{spi:x} """.format(**locals())

print(table)
