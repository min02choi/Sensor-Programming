import RPi.GPIO as GPIO
import signal
import sys
import time

counter = 0


def signal_handler(signal, frame):
    print('process stop')
    GPIO.cleanup()
    sys.exit(0)


# count 값을 늘려줌
def my_callback(channel):
    global eventCounter
    eventCounter += 1
    global humandetect
    humandetect = 1


signal.signal(signal.SIGINT, signal_handler)

GPIO.setmode(GPIO.BCM)  # BCM Mode

MOTION_IN = 27          # GPIO 27(Wpi : 2)
eventCounter = 0
humandetect = 0

GPIO.setup(MOTION_IN, GPIO.IN)

# event 방식. loop를 돌면서 대기하지 않음
# GPIO.RISING: Low -> High로 변화가 일어날 때 감지, callback 함수 호출
# 무엇인가 지나갈 때 호출
GPIO.add_event_detect(MOTION_IN, GPIO.RISING, callback=my_callback)
GPIO.add_event_detect(MOTION_IN, )

while True:
    if humandetect == 1:
        print("Detect %d" % eventCounter)
        humandetect = 0

        while GPIO.input(MOTION_IN):
            counter += 1
            print("high %d " % counter)
            time.sleep(1)
        counter = 0
    else:
        print("No detect")

    time.sleep(0.5)
