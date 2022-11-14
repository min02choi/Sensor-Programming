import smbus
import time

bus = smbus.SMBus(1)
addr = 0x20
port_config = 0x06
port_output = 0x02
digit = (0x7F, 0xBF, 0xDF, 0xEF, 0xF7, 0xFB)
segment = (0xFC, 0x60, 0xDA, 0xF2, 0x66, 0xB6, 0x3E, 0xE0, 0xFE, 0xF6, 0x01)
word_code = 0

try:
    bus.write_word_data(addr, port_config, 0x0000)

    while True:
        n1 = time.ctime()[11:13]
        n2 = time.ctime()[14:16]
        n3 = time.ctime()[17:19]
        n_total = n1 + n2 + n3

        word_code = segment[10] << 8 | digit[1]
        bus.write_word_data(addr, port_output, word_code)
        word_code = segment[10] << 8 | digit[3]
        bus.write_word_data(addr, port_output, word_code)

        for i in range(len(digit)):
            n = int(n_total[i])
            word_code = segment[n] << 8 | digit[i]
            bus .write_word_data(addr, port_output, word_code)
            time.sleep(0.005)   # 한 번에 하나만 되기 떄문에 겁나 빨리해서

except KeyboardInterrupt:
    bus.write_word_data(addr, port_config, 0x0000)
    pass
