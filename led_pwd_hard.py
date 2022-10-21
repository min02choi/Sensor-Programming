import RPi.GPIO as GPIO
from time import sleep

PIN_LED = 12                        # LED 모듈이 연결된 핀 번호(BCM 12번 핀)
GPIO.setmode(GPIO.BCM)              # BCM 모드
GPIO.setup(PIN_LED, GPIO.OUT)       # 12번 핀을 출력모 드로 설정
pi_pwm = GPIO.PWM(PIN_LED, 1000)    # PIN_LED를 PWM 모드로 할 것임, 1000 << 시간 지정
pi_pwm.start(0)                     # low 신호부터 시작

try:
    while True:
        for duty in range(0, 101, 1):       # 점점 증가함(점점 밝아짐), 마치 아날로그 신호처럼 보임
            pi_pwm.ChangeDutyCycle(duty)    # 시간이 늘어남
            sleep(0.01)
        sleep(0.5)                          # 완전 켜진 상태 유지

        for duty in range(100, -1, -1):     # 점점 작아짐 (점점 어두어짐)
            pi_pwm.ChangeDutyCycle(duty)    # 시간이 줄어들음
            sleep(0.01)
        sleep(0.5)                          # 완전 꺼진 상태 유지
except KeyboardInterrupt:
    print("Cleaning up")
    GPIO.cleanup()