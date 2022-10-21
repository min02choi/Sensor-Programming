import RPi.GPIO as GPIO
import time
import signal
import sys


def signal_handler(signal, frame):
    print('process stop')
    PWM_RC.stop()
    GPIO.cleanup()
    sys.exit(0)


RCSERVO = 23        # GPIO 23(Wpi : 4)
GPIO.setup(RCSERVO, GPIO.OUT)
PWM_RC = GPIO.PWM(RCSERVO, 100)
PWM_RC.start(7.5)

signal.signal(signal.SIGINT, signal_handler)
GPIO.setmode(GPIO.BCM)      # BCM Mode

GPIO.setmode(GPIO.BCM)

# HC-SR04의 트리거 핀을 GPIO 17번, 에코핀을 GPIO 27번에 연결한다.
GPIO_TRIGGER = 18   # 17
GPIO_ECHO = 21      # 27

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)


try:
    while True:
        stop = 0
        start = 0

        GPIO.output(GPIO_TRIGGER, False)  # 먼저 트리거 핀을 OFF 상태로 유지한다
        time.sleep(2)

        GPIO.output(GPIO_TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)

        while GPIO.input(GPIO_ECHO) == 0:
            start = time.time()

        while GPIO.input(GPIO_ECHO) == 1:
            stop = time.time()

        elapsed = stop - start

        if (stop and start):
            distance = (elapsed * 34000.0) / 2
            print("Distance : %.1f cm" % distance)

            if (distance <= 10):
                PWM_RC.ChangeDutyCycle(5)  # 5는 해당 모터가 돌아와야 하는 위치임
                time.sleep(1)
                PWM_RC.ChangeDutyCycle(95)
                time.sleep(1)

except KeyboardInterrupt:
    print("Ultrasonic Distance Measurement End")
    GPIO.cleanup()
