import RPi.GPIO as GPIO
import time
import signal
import sys

# 사용자의 입력값에 따라 선풍기 틀음
# time.sleep(초)를 통해 특정시간동안 fan on, stop_fan_led함수를 통해 그 시간이 정하면 꺼지게 함

def signal_handler(signal, frame):
    print('process stop')
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def setRGB(r, g, b):
    PWM_RED.ChangeDutyCycle(r)
    PWM_GREEN.ChangeDutyCycle(g)
    PWM_BLUE.ChangeDutyCycle(b)

def stop_fan_led():
    setRGB(0, 0, 0)
    PWM_Fan.ChangeDutyCycle(0)

GPIO.setmode(GPIO.BCM)

# LED를 PWM으로 설정
ledRed = 4
ledGreen = 3
ledBlue = 2

GPIO.setup(ledRed, GPIO.OUT)
GPIO.setup(ledGreen, GPIO.OUT)
GPIO.setup(ledBlue, GPIO.OUT)

PWM_RED = GPIO.PWM(ledRed, 100)
PWM_RED.start(0)

PWM_GREEN = GPIO.PWM(ledGreen, 100)
PWM_GREEN.start(0)

PWM_BLUE = GPIO.PWM(ledBlue, 100)
PWM_BLUE.start(0)

# Fan을 PWM으로 설정
fan = 6

GPIO.setup(fan, GPIO.OUT)
PWM_Fan = GPIO.PWM(fan, 100)
PWM_Fan.start(0)


user = ""
try:
    while True:
        user = input("Enter the level of fan(low/middle/high/off): ")

        if (user == "low"):
            setRGB(100, 0, 0)
            PWM_Fan.ChangeDutyCycle(20)
            # time.sleep(3)
            # stop_fan_led()
        elif (user == "middle"):
            setRGB(0, 100, 0)
            PWM_Fan.ChangeDutyCycle(50)
            # time.sleep(3)
            # stop_fan_led()
        elif (user == "high"):
            setRGB(0, 0, 100)
            PWM_Fan.ChangeDutyCycle(100)
            # time.sleep(3)
            # stop_fan_led()
        elif (user == "off"):
            signal_handler(0, 0)        # 매개변수 안씀

except KeyboardInterrupt:
    print("Program end")
    GPIO.cleanup()

