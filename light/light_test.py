import RPi.GPIO as GPIO
import signal
import sys
import time


def signal_handler(signal, frame):
    print("process stop")
    GPIO.cleanup()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
GPIO.setmode(GPIO.BCM)      # BCM Mode
LIGHTSEN_OUT = 27           # GPIO 27 (Wpi : 2)
GPIO.setup(LIGHTSEN_OUT, GPIO.IN)

while True:
    if GPIO.input(LIGHTSEN_OUT) == 0:
        print("light full !")
    if GPIO.input(LIGHTSEN_OUT) == 1:
        print("dark")
    time.sleep(1)
