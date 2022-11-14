import spidev
import RPi.GPIO as GPIO
import time

# 이 코드 문제가 있음. 500이 기준인데 이 500이 무슨 의미인지 알 길이 없음

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000

led_pin1 = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setwarnings(False)


def analog_read(channel):
    r = spi.xfer2([1, (8 + channel) << 4, 0])
    adc_out = ((r[1] & 3) << 8) + r[2]
    return adc_out


print("start")

try:
    while True:
        reading = analog_read(1)
        voltage = reading * 3.3 / 1024
        print("light sensor = %f" %(reading))

        if (reading > 500.0):       # 500이 무슨 의미인지 알 수 없음. 룩스(럭스)는 아님
            GPIO.output(led_pin1, True)
        else:
            GPIO.output(led_pin1, False)
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Program is terminated...!")

finally:
    print("cleaning up")
    GPIO.cleanup()
