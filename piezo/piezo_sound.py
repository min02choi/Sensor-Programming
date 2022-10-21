import RPi.GPIO as GPIO
import signal
import sys
import time

# 부저는 압전의 원리임


def signal_handler(signal, frame):      # event handler. 콜백 함수. 언제 호출될 지 모름
    print("process stop")
    GPIO.cleanup()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)    # terminal에서 ctrl+c 는 1번
GPIO.setmode(GPIO.BCM)      # BCM Mode
BUZCONTROL = 20             # GPIO 20 (Wpi : 28)
GPIO.setup(BUZCONTROL, GPIO.OUT)

while True:
    print("here")
    GPIO.output(BUZCONTROL, 1)
    time.sleep(1)
    GPIO.output(BUZCONTROL, 0)
    time.sleep(1)
