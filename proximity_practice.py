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

COLLISION = 22              # GPIO 22(Wpi : 3)
BUZZER = 20                 # 부저 번호

GPIO.setup(COLLISION, GPIO.IN)
GPIO.setup(BUZZER, GPIO.OUT)

# 기본 값은 1임
while True:
    if GPIO.input(COLLISION) == 0:     # Falling Edge
        print("Careful~~~ oops")
        GPIO.output(BUZZER, 1)
    if GPIO.input(COLLISION) == 1:
        print("Not Collision...")
        GPIO.output(BUZZER, 0)

    time.sleep(0.2)
