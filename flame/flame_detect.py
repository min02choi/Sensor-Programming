import RPi.GPIO as GPIO
import signal
import sys
import time


def signal_handler(signal, frame) :
    print('process stop')
    GPIO.cleanup()
    sys.exit(0)


def my_callback(channel):
    global eventCounter
    eventCounter += 1


signal.signal(signal.SIGINT, signal_handler)

GPIO.setmode(GPIO.BCM)      # BCM Mode

FLAME_IN = 24               # GPIO 24(Wpi : 5)
eventCounter = 0

GPIO.setup(FLAME_IN, GPIO.IN)
GPIO.add_event_detect(FLAME_IN, GPIO.FALLING, callback=my_callback)

while True:
    print("%d" %eventCounter)
    time.sleep(1)