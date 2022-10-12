import RPi.GPIO as GPIO
import time

pin = 13    # PWM pin num 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
p = GPIO.PWM(pin, 50)
p.start(0)
cnt = 0

try:
    while True:
        p.ChangeDutyCycle(1)    # 5 * 0.01 = 0.05v
        print("angle : 1")
        time.sleep(5)
        p.ChangeDutyCycle(5)    # 5 * 0.05 = 0.25v
        print("angle : 5")
        time.sleep(5)
        p.ChangeDutyCycle(8)
        print("angle : 8")
        time.sleep(5)

except KeyboardInterrupt:
    p.stop()

GPIO.cleanup()
