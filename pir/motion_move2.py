import RPi.GPIO as GPIO
import time

motion_in = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(motion_in, GPIO.IN)


def loop():
    cnt = 0

    # loop를 돌면서 값을 0.1초 간격으로 확인
    # motion_move.py와는 다른 방식
    while True:
        if (GPIO.input(motion_in) == True):
            print('detected %d' % cnt)
            cnt += 1
        time.sleep(0.1)


try:
    loop()
except KeyboardInterrupt:
    pass
    print("Sensing is terminated....!!!")
finally:
    GPIO.cleanup()
