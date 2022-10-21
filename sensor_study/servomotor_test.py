import time

import RPi.GPIO as GPIO
import signal
import sys



def signal_handler(signal, frame):
    print('process stop')
    PWM_servo.stop()
    GPIO.cleanup()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


def setAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(23, True)
	PWM_servo.ChangeDutyCycle(duty)
	time.sleep(1)
	GPIO.output(23, False)
	PWM_servo.ChangeDutyCycle(0)


GPIO.setmode(GPIO.BCM)      # BCM Mode

servo = 23
GPIO.setup(servo, GPIO.OUT)
PWM_servo = GPIO.PWM(servo, 50)
PWM_servo.start(0)

num = 0;

while True:
    num = int(input("enter the num: "))
    setAngle(90)
    time.sleep(1)
