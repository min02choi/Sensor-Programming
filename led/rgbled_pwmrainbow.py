import RPi.GPIO as GPIO
import signal
import sys
import time


def signal_handler(signal, frame):
    print('process stop')
    GPIO.cleanup()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

GPIO.setmode(GPIO.BCM)      # BCM Mode

RGBLEDPOWER = 12            # GPIO 12(Wpi : 26)

RED = 4         # GPIO 4 (Wpi : 8)
GREEN = 3       # GPIO 3 (Wpi : 9)
BLUE = 2        # GPIO 2 (Wpi : 7)

GPIO.setup(RGBLEDPOWER, GPIO.OUT)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

PWM_RED = GPIO.PWM(RED, 500)
PWM_RED.start(100)

PWM_GREEN = GPIO.PWM(GREEN, 500)
PWM_GREEN.start(100)

PWM_BLUE = GPIO.PWM(BLUE, 500)
PWM_BLUE.start(100)


def setRGB(r, g, b):
    PWM_RED.ChangeDutyCycle(r)
    PWM_GREEN.ChangeDutyCycle(g)
    PWM_BLUE.ChangeDutyCycle(b)


while True:
    print("RGB LED Various Color")

    GPIO.output(RGBLEDPOWER, 1)

    setRGB(100, 0, 0)
    time.sleep(1)
    setRGB(100, 20, 0)
    time.sleep(1)
    setRGB(100, 100, 0)
    time.sleep(1)
    setRGB(0, 100, 0)
    time.sleep(1)
    setRGB(0, 0, 100)
    time.sleep(1)
    setRGB(0, 4, 100)
    time.sleep(1)
    setRGB(40, 0, 100)
    time.sleep(1)


# 빨: 100, 0, 0
# 주: 100, 20, 0
# 노: 100, 100, 0
# 초: 0, 100, 0
# 파: 0, 0, 100
# 남: 0, 4, 100
# 보: 40, 0, 100
