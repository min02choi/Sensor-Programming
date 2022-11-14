import smbus
import time

bus = smbus.SMBus(1)
addr = 0x20
port_config = 0x06
port_output = 0x02


digit = (0x7F, 0xBF, 0xDF, 0xEF, 0xF7, 0xFB, 0xF7, 0xEF, 0xDF, 0xBF, 0x7F)
segment = (0xEE, 0xFE, 0x9C, 0x7A, 0x9E, 0x8E, 0xBE, 0x6E, 0x60, 0x78, 0x1C, 0xFC, 0xCE, 0xB6, 0x7C)
word_code = 0

try:
    bus.write_word_data(addr, port_config, 0x0000)

    for i in range(len(segment)):
        for j in range(len(digit)):
            word_code = segment[i] << 8 | digit[j]      # 8비트 두개를 붙이는 작업
            bus.write_word_data(addr, port_output, word_code)
            print("%x " % word_code)
            # bus.write_word_data(addr, port_output, word_code)
            time.sleep(0.15)
except KeyboardInterrupt:
    pass
