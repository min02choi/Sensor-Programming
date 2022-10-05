import RPi.GPIO as GPIO
import time

PIN_LED = 12                    # BCM 12번 핀에 해당

GPIO.setmode(GPIO.BCM)          # BOARD, BCM 2가지 모드가 있음
GPIO.setup(PIN_LED, GPIO.OUT)   # LED가 연결된 핀을 출력으로 설정

def blink(Num):
    for i in range(1, Num):
        GPIO.output(PIN_LED, GPIO.HIGH)
        time.sleep(i)
        GPIO.output(PIN_LED, GPIO.LOW)
        time.sleep(1)

In = int(input("Give times you want: "))    # 입력값은 문자열로 들어오므로 int로 형 변환
blink(In)
print("Program is terminated!")
GPIO.cleanup()
