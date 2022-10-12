import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO_RP = 13
GPIO.setup(GPIO_RP, GPIO.OUT)

try:
    while True:
        print("forward")
        GPIO.output(GPIO_RP, True)
        time.sleep(1)
        print("stop")
        GPIO.output(GPIO_RP, False)
        time.sleep(5)
except KeyboardInterrupt:
    print("Motor activation is terminated....!!!")
finally:
    GPIO.cleanup()
