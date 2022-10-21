import RPi.GPIO as GPIO
import signal
import sys
import time


def signal_handler(signal, frame):
    print('process stop')
    PWM_RC.stop()
    GPIO.cleanup()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


GPIO.setmode(GPIO.BCM)      # BCM Mode

RCSERVO = 23        # GPIO 23(Wpi : 4)

GPIO.setup(RCSERVO, GPIO.OUT)
PWM_RC = GPIO.PWM(RCSERVO, 100)
PWM_RC.start(7.5)

while True:
    print("here - RCMOTOR on")
    PWM_RC.ChangeDutyCycle(5)   # 5는 해당 모터가 돌아와야 하는 위치임
    time.sleep(1)
    PWM_RC.ChangeDutyCycle(95)
    time.sleep(1)

# PWM_RC.ChangeDutyCycle(5) -> 숫자 값을 주면 위치가 정해져있음
# DutyCycle을 크게 준다고 해서 많이 도는게 아님.
# 정밀 조작을 위한 센서이므로 반드시 PWM을 이용하여 조작
