import RPi.GPIO as GPIO
import signal
import sys
import time


def signal_handler(signal, frame) :
    print('process stop')
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

GPIO.setmode(GPIO.BCM)      # BCM Mode

FAN = 6                 # GPIO 6(Wpi : 22)

GPIO.setup(FAN, GPIO.OUT)

while True:
    # print("here - FAN on")
    GPIO.output(FAN, 1)