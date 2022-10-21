import RPi.GPIO as GPIO
import time

# 거리가 가까워지면 모터가 빠르게 돌음

def detect_distance():
    GPIO.output(ultra_trig, False)
    time.sleep(0.5)

    GPIO.output(ultra_trig, True)
    time.sleep(0.00001)
    GPIO.output(ultra_trig, False)

    while GPIO.input(ultra_echo) == 0:
        pulse_start = time.time()
    while GPIO.input(ultra_echo) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    dist = pulse_duration * 17000
    return round(dist, 2)


GPIO.setmode(GPIO.BCM)

# ultrasonic sensor
ultra_trig = 18
ultra_echo = 21

GPIO.setup(ultra_trig, GPIO.OUT)
GPIO.setup(ultra_echo, GPIO.IN)

# dcmotor
dcmotor = 13
GPIO.setup(dcmotor, GPIO.OUT)
PWM_dcmotor = GPIO.PWM(dcmotor, 50)

PWM_dcmotor.start(0)
PWM_dcmotor.ChangeDutyCycle(0)

# 변수 선언
distance = 0

try:
    while True:
        distance = detect_distance()

        if (distance <= 30):
            PWM_dcmotor.ChangeDutyCycle((30 - distance) / 1.5)
        else:
            PWM_dcmotor.ChangeDutyCycle(0)
except KeyboardInterrupt:
    GPIO.cleanup()


