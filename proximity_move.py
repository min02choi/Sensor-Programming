import RPi.GPIO as GPIO
import signal
import sys
import time


def signal_handler(signal, frame):
    print('process stop')
    GPIO.cleanup()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)    # try-except 안쓰고 이거 사용

GPIO.setmode(GPIO.BCM)      # BCM Mode

COLLISION = 22              # GPIO 22(Wpi : 3)

GPIO.setup(COLLISION, GPIO.IN)

while True:
    if GPIO.input(COLLISION) == 0:      # 수신부의 결과를 획득
        print("Careful~~~ oops")
    if GPIO.input(COLLISION) == 1:      # 기본 상태가 1임
        print("Not Collision...")
    time.sleep(0.2)
