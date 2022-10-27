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

PUMP = 5        # GPIO 5(Wpi : 21)

GPIO.setup(PUMP, GPIO.OUT)

while True:
    print("here - PUMP on")
    GPIO.output(PUMP, 1)
    time.sleep(2)
    print("here - PUMP off")
    GPIO.output(PUMP, 0)
    time.sleep(2)
