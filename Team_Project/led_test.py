import RPi.GPIO as GPIO
import time
import signal
import sys
import threading

# 시스템 종료
def signal_handler(signal, frame):
    print('process stop')
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


#### LED ####
# LED 색 RGB 설정
def setRGB(r, g, b):
    PWM_RED.ChangeDutyCycle(r)
    PWM_GREEN.ChangeDutyCycle(g)
    PWM_BLUE.ChangeDutyCycle(b)

# LED 깜빡임
def led_action():
    # 정하셈 변수들을 global로 뺼지 말지
    # 근데 LEVEL도 안 빼도 될거같긴 함
    global LEVEL
    global rgb_color
    global led_speed

    # 1단계, 2단계, 3단계 LED가 켜지는 시간을 조절할 것 (led_speed)
    # time.sleep(led_speed), time.sleep(1 - led_speed) 이런 느낌으로
    while True:
        if (LEVEL == 0):
            setRGB(0, 0, 0)
        if (LEVEL == 1):
            setRGB(rgb_color[0], rgb_color[1], rgb_color[2])
            time.sleep(led_speed)
            setRGB(0, 0, 0)
            time.sleep(0.5)
        if (LEVEL == 2):
            setRGB(rgb_color[0], rgb_color[1], rgb_color[2])
            time.sleep(led_speed)
            setRGB(0, 0, 0)
            time.sleep(0.3)
        if (LEVEL == 3):
            setRGB(rgb_color[0], rgb_color[1], rgb_color[2])
            time.sleep(led_speed)
            setRGB(0, 0, 0)
            time.sleep(0.2)


################### 센서&변수 세팅 ################################


GPIO.setmode(GPIO.BCM)

#### MQ7 세팅 ####

CO_STATE = 0


#### LED 세팅 ####
ledRed = 11
ledGreen = 9
ledBlue = 10

GPIO.setup(ledRed, GPIO.OUT)
GPIO.setup(ledGreen, GPIO.OUT)
GPIO.setup(ledBlue, GPIO.OUT)

PWM_RED = GPIO.PWM(ledRed, 100)
PWM_RED.start(0)

PWM_GREEN = GPIO.PWM(ledGreen, 100)
PWM_GREEN.start(0)

PWM_BLUE = GPIO.PWM(ledBlue, 100)
PWM_BLUE.start(0)

# 구체적인 RGB설정을 위함
# red_num = 0
# green_num = 0
# blue_num = 0
rgb_color = [0, 0, 0]       # RGB 색 설정

# LED 깜빡이는 속도
led_speed = 0

#### Piezo ####
piezo = 23
GPIO.setup(piezo, GPIO.OUT)
PWM_Piezo = GPIO.PWM(piezo, 100)
PWM_Piezo.start(0)

LEVEL = 0

##################### 코드 시작 ##############################

try:
    # 쓰레드 실행
    thread1_LED = threading.Thread(target=led_action, daemon=True)
    thread1_LED.start()

    # state 설정
    #

    while True:
        # 일단은 사용자 input으로 값을 받아 실험
        LEVEL = int(input("Enter the Level: "))

        # LEVEL 값에 따른 작동
        if (LEVEL == 0):
            rgb_color = [0, 0, 0]
            # 택트 버튼 누를 경우 LEVEL 값을 0으로 설정

        #### 1단계 ####
        if (LEVEL == 1):
            ## LED 설정 ##
            rgb_color = [255, 255, 0]   # 색 수치만 넣으면 됨
            led_speed = 1               # LED 깜빡이는 속도

        #### 2단계 ####
        if (LEVEL == 2):
            rgb_color = [255, 130, 0]   # 색 수치만 넣으면 됨
            led_speed = 0.6             # LED 깜빡이는 속도

        #### 3단계 ####
        if (LEVEL == 3):
            rgb_color = [255, 0, 0]     # 색 수치만 넣으면 됨
            led_speed = 0.3             # LED 깜빡이는 속도


except KeyboardInterrupt:
    print("Program End")
