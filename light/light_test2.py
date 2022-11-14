import spidev
import time

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000


def analog_read(channel):
    r = spi.xfer2([1, (8 + channel) << 4, 0])   #
    adc_out = ((r[1] & 3) << 8) + r[2]
    return adc_out


print("start")

while True:
    reading = analog_read(1)
    voltage = reading * 3.3 / 1024
    print("light sensor = %f" %(reading))       # 어두울수록 출력값이 커진다.
    time.sleep(0.1)

"""
    converter 안의 값이 10비트로 옴
    2^10 = 65536 -> 럭스(?)
"""