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
RGBLEDPOWER = 19            # GPIO 19(Wpi : 24), 전원 공급

RED = 4         # GPIO 2 (Wpi : 8)
GREEN = 3       # GPIO 3 (Wpi : 9)
BLUE = 2        # GPIO 4 (Wpi : 7)

GPIO.setup(RGBLEDPOWER, GPIO.OUT)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

for i in range(0, 10):
    GPIO.output(RGBLEDPOWER, 1)

    GPIO.output(RED, 1)
    GPIO.output(BLUE, 0)
    GPIO.output(GREEN, 0)

    time.sleep(1)

    GPIO.output(RED, 0)
    GPIO.output(BLUE, 1)
    GPIO.output(GREEN, 0)

    time.sleep(1)

    GPIO.output(RED, 1)
    GPIO.output(BLUE, 0)
    GPIO.output(GREEN, 1)

    time.sleep(1)

    GPIO.output(RED, 1)
    GPIO.output(BLUE, 1)
    GPIO.output(GREEN, 1)

    time.sleep(1)

GPIO.output(GREEN, 0)
