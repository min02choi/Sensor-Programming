import RPi.GPIO as GPIO
from time import sleep

PIN_LED = 12                        # LED 모듈이 연결된 핀 번호(BCM 12번 핀)
GPIO.setmode(GPIO.BCM)              # BCM 모드
GPIO.setup(PIN_LED, GPIO.OUT)       # 12번 핀을 출력모 드로 설정
pi_pwm = GPIO.PWM(PIN_LED, 1000)
pi_pwm.start(0)

try:
    while True:
        for duty in range(0, 101, 1):
            pi_pwm.ChangeDutyCycle(duty)
            sleep(0.01)
        sleep(0.5)

        for duty in range(100, -1, -1):
            pi_pwm.ChangeDutyCycle(duty)
            sleep(0.01)
        sleep(0.5)
except KeyboardInterrupt:
    print("Cleaning up")
    GPIO.cleanup()