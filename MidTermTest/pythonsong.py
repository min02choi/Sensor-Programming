import RPi.GPIO as GPIO
import time

def led_blink(t):
    GPIO.output(PIN_LED, GPIO.HIGH)
    time.sleep(t)

def led_off():
    GPIO.output(PIN_LED, GPIO.LOW)
    time.sleep(0.1)

def sound_out(s, t):
    p.ChangeFrequency(scale[s])
    time.sleep(0.5)



GPIO.setmode(GPIO.BCM)
gpio_pin = 20                     # BCM: 20
GPIO.setup(gpio_pin, GPIO.OUT)

scale = [261, 294, 329, 349, 392, 440, 493, 523]      # do, rae, mi, pa~~~
down_scale = [130, 146, 164, 174, 195, 220, 246, 261]
p = GPIO.PWM(gpio_pin, 100)
GPIO.output(gpio_pin, True)
p.start(100)                    # start the PWM on 100% duty cycle
p.ChangeDutyCycle(20)           # change the duty cycle to 90%. 음절을 만들기 위해

# led
PIN_LED = 12                    # BCM 12번 핀에 해당

GPIO.setmode(GPIO.BCM)          # BOARD, BCM 2가지 모드가 있음
GPIO.setup(PIN_LED, GPIO.OUT)   # LED가 연결된 핀을 출력으로 설정

def make_sound(s, t):
    global scale

    GPIO.output(PIN_LED, GPIO.HIGH)
    p.ChangeDutyCycle(20)       # 고전 값
    p.ChangeFrequency(scale[s])
    time.sleep(t)
    GPIO.output(PIN_LED, GPIO.LOW)
    p.ChangeDutyCycle(0)
    time.sleep(0.1)

try:
    make_sound(4, 0.5)
    make_sound(4, 0.5)
    make_sound(5, 0.5)
    make_sound(5, 0.5)
    make_sound(4, 0.5)
    make_sound(4, 0.5)
    make_sound(2, 1)

    make_sound(4, 0.5)
    make_sound(4, 0.5)
    make_sound(2, 0.5)
    make_sound(2, 0.5)
    make_sound(1, 2)



except KeyboardInterrupt:
    print("Cleaning up")
    GPIO.cleanup()              # GPIO 초기화
