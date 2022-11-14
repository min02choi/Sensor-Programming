import smbus
import time

bus = smbus.SMBus(1)
addr = 0x20
port_config = 0x06
port_output = 0x02

digit = (0x1F, 0xE3, 0x1F, 0xE3)
segment = (0xFC, 0x60, 0xDA, 0xF2)
alpha = (0xEE, 0x3E, 0x9C, 0x7A)
word_code = 0

try:
    bus.write_word_data(addr, port_config, 0x0000)

    for i in range(len(alpha)):
        word_code = alpha[i] << 8 | digit[i]  # 8비트 두개를 붙이는 작업
        bus.write_word_data(addr, port_output, word_code)
        time.sleep(1)

    # for j in range(len(alpha)):
    #     for i in range(len(digit)):
    #         word_code = alpha[j] << 8 | digit[i]      # 8비트 두개를 붙이는 작업
    #         bus.write_word_data(addr, port_output, word_code)
    #         print("%x " % word_code)
    #         # bus.write_word_data(addr, port_output, word_code)
    #         time.sleep(1)

except KeyboardInterrupt:
    pass
