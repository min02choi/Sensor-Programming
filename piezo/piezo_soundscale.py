import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
gpio_pin = 20
scale = [261, 294, 329, 349, 392, 440, 493, 523]
# scale = [130, 146, 164, 174, 195, 220, 246, 261]
# scale = [32, 36, 41, 43, 48, 55, 61, 65]

GPIO.setup(gpio_pin, GPIO.OUT)

try:
    p = GPIO.PWM(gpio_pin, 10)
    p.start(100)                # start the PWM on 100% duty cycle
    p.ChangeDutyCycle(10)       # change the duty cycle to 90%

    for i in range(8):
        print(i + 1)
        p.ChangeFrequency(scale[i])
        time.sleep(1)
    p.stop()                    # stop the PWM output
finally:
    GPIO.cleanup()
