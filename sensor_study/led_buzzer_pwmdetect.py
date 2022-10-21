import RPi.GPIO as GPIO
import time
import signal
import sys

# 거리에 따라 불빛과 소리의 크기(changeDutyCycle)가 달라지는 자동차 후방 감지기

def signal_handler(signal, frame):
    print('process stop')
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# 거리를 측정하여 거리를 리턴함
def detect_distance():
    GPIO.output(ultra_trig, False)
    time.sleep(0.5)

    GPIO.output(ultra_trig, True)
    time.sleep(0.00001)
    GPIO.output(ultra_trig, False)

    while GPIO.input(ultra_echo) == 0:
        pulse_start = time.time()
        # print("hello1")
    while GPIO.input(ultra_echo) == 1:
        pulse_end = time.time()
        # print("hello2")

    pulse_duration = pulse_end - pulse_start
    dist = pulse_duration * 17000
    return round(dist, 2)

# RGB색 설정
def setRGB(r, g, b):
    PWM_RED.ChangeDutyCycle(r)
    PWM_GREEN.ChangeDutyCycle(g)
    PWM_BLUE.ChangeDutyCycle(b)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)     # 뭔지는 모르겠지만

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

# Buzzer PWM설정
piezo = 20
GPIO.setup(piezo, GPIO.OUT)
PWM_piezo = GPIO.PWM(piezo, 100)
PWM_piezo.start(0)

# Ultrasonic 설정
ultra_trig = 18   # 3
ultra_echo = 21   # 4

GPIO.setup(ultra_trig, GPIO.OUT)
GPIO.setup(ultra_echo, GPIO.IN)


try:
    while True:
        distance = detect_distance()
        print(distance)

        if (distance <= 5):
            setRGB(100, 0, 0)
            PWM_piezo.ChangeDutyCycle(80)

        elif (distance <= 10):
            setRGB(100, 20, 0)
            PWM_piezo.ChangeDutyCycle(40)

        elif (distance <= 20):
            setRGB(100, 100, 0)
            PWM_piezo.ChangeDutyCycle(10)
        else:
            setRGB(0, 100, 0)
            PWM_piezo.ChangeDutyCycle(0)

except KeyboardInterrupt:
    print("Program end")
    GPIO.cleanup()
