import threading

import RPi.GPIO as GPIO
import signal
import sys
import time

# PIR: 터치를 안하면 1인 상태(1이 기본 상태)
# 1: 기본 상태, 0: 변화가 일어난 상태

def ledBlink():
    global flag

    while True:
        if (flag == 0):
            GPIO.output(led, False)
            time.sleep(0.2)
            GPIO.output(led, True)
            time.sleep(0.2)
        elif (flag == 1):
            GPIO.output(led, False)

GPIO.setmode(GPIO.BCM)

# led센서
led = 12
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, False)

# pir 센서
pir = 22
GPIO.setup(pir, GPIO.IN)

# 공유변수 선언
flag = 1

try:
    t1 = threading.Thread(target=ledBlink, daemon=True)
    t1.start()

    while True:
        if (GPIO.input(pir) == 0):      # 터치가 되었을 때
            flag = 0                    # 터치가 안 된 상태
            print("detected")
        else:
            flag = 1
            print("not detected")
        time.sleep(1)


except KeyboardInterrupt:
    GPIO.cleanup()
