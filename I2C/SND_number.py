import smbus
import time

bus = smbus.SMBus(1)
addr = 0x20
port_config = 0x06
port_output = 0x02

# digit = (0x7F, 0xBF, 0xDF, 0xEF, 0xF7, 0xFB)
digit = (0x03, 0x03, 0x03, 0x03, 0x03, 0x03)
segment = (0xFC, 0x60, 0xDA, 0xF2, 0x66, 0xB6, 0x3E, 0xE0, 0xFE, 0xF6)
word_code = 0

try:
    bus.write_word_data(addr, port_config, 0x0000)

    for i in range(len(digit)):
        for j in range(len(segment)):
            word_code = segment[j] << 8 | digit[i]      # 8비트 두개를 붙이는 작업
            print("%x " % word_code)
            bus.write_word_data(addr, port_output, word_code)
            time.sleep(1)
except KeyboardInterrupt:
    pass
