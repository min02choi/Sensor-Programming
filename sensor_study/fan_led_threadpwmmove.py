import RPi.GPIO as GPIO
import time
import signal
import sys
import threading

# 사용자의 입력값에 따라 선풍기 틀음
# time.sleep(초)를 통해 특정시간동안 fan on, stop_fan_led함수를 통해 그 시간이 정하면 꺼지게 함
# thread를 사용하여 fan을 돌림과 동시에 led깜빡임, buzzer
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

def ledRGB_OnOff():
    global flag
    global red_num
    global green_num
    global blue_num
    global t

    while True:
        setRGB(red_num, green_num, blue_num)
        time.sleep(t)
        setRGB(0, 0, 0)
        time.sleep(t)

def buzzer_OnOff():
    global PWM_Piezo
    global piezo_time
    global user

    while True:
        if (user == "high"):
            PWM_Piezo.ChangeDutyCycle(5)
            PWM_Piezo.ChangeFrequency(400)
        elif (user == "middle"):
            PWM_Piezo.ChangeDutyCycle(5)
            PWM_Piezo.ChangeFrequency(300)
        elif (user == "low"):
            PWM_Piezo.ChangeDutyCycle(5)
            PWM_Piezo.ChangeFrequency(200)
        else:
            PWM_Piezo.ChangeDutyCycle(0)

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

# 색 실험
red_num = 0
green_num = 0
blue_num = 0

t = 0

# Fan을 PWM으로 설정
fan = 6

GPIO.setup(fan, GPIO.OUT)
PWM_Fan = GPIO.PWM(fan, 100)
PWM_Fan.start(0)

# piezo센서 pwm
piezo = 20
GPIO.setup(piezo, GPIO.OUT)
PWM_Piezo = GPIO.PWM(piezo, 100)
PWM_Piezo.start(0)

piezo_time = 0

flag = 0

user = ""
try:
    t1 = threading.Thread(target=ledRGB_OnOff, daemon=True)
    t1.start()
    t2 = threading.Thread(target=buzzer_OnOff, daemon=True)
    t2.start()
    while True:
        user = input("Enter the level of fan(low/middle/high/off): ")

        if (user == "low"):
            red_num = 100
            green_num = 0
            blue_num = 0
            t = 1.5
            PWM_Fan.ChangeDutyCycle(20)
        elif (user == "middle"):
            red_num = 100
            green_num = 20
            blue_num = 0
            t = 1
            PWM_Fan.ChangeDutyCycle(50)
        elif (user == "high"):
            red_num = 0
            green_num = 50
            blue_num = 0
            t = 0.5
            PWM_Fan.ChangeDutyCycle(100)
        elif (user == "off"):
            signal_handler(0, 0)        # 매개변수 안씀

except KeyboardInterrupt:
    print("Program end")
    GPIO.cleanup()

