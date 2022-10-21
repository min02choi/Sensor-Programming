import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

trig = 18   # 3
echo = 21   # 4

print("start")

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

try:
    while True:
        GPIO.output(trig, False)
        time.sleep(2)

        GPIO.output(trig, True)
        time.sleep(0.00001)
        GPIO.output(trig, False)

        while GPIO.input(echo) == 0:
            pulse_start = time.time()
            # print("hello1")
        while GPIO.input(echo) == 1:
            pulse_end = time.time()
            # print("hello2")

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17000
        distance = round(distance, 2)

        print("Distance:", distance, "cm")
except:
    GPIO.cleanup()
