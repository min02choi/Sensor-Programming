import RPi.GPIO as GPIO
import time

PIN_LED = 12                    # BCM 12번 핀에 해당

GPIO.setmode(GPIO.BCM)          # BOARD, BCM 2가지 모드가 있음
GPIO.setup(PIN_LED, GPIO.OUT)   # LED가 연결된 핀을 출력으로 설정

try:
    while True:
        GPIO.output(PIN_LED, False)     # LOW 신호(0V)를 전송
        time.sleep(1)                   # 1초 동안 딜레이

        GPIO.output(PIN_LED, True)      # HIGH 신호(5V)를 전송
        time.sleep(1)

except KeyboardInterrupt:
    print("Cleaning up")
    GPIO.cleanup()              # GPIO 초기화
