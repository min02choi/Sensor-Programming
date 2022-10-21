import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
gpio_pin = 20                     # BCM: 20
GPIO.setup(gpio_pin, GPIO.OUT)

scale = [261, 294, 329, 349, 392, 440, 493, 523]      # do, rae, mi, pa~~~
down_scale = [130, 146, 164, 174, 195, 220, 246, 261]
p = GPIO.PWM(gpio_pin, 100)
GPIO.output(gpio_pin, True)
p.start(100)                    # start the PWM on 100% duty cycle
p.ChangeDutyCycle(20)           # change the duty cycle to 90%. 음절을 만들기 위해

while True:
    p.ChangeFrequency(scale[4])
    time.sleep(0.8)
    p.ChangeFrequency(scale[2])
    time.sleep(0.4)
    p.ChangeFrequency(scale[3])
    time.sleep(0.4)
    p.ChangeFrequency(scale[4])
    time.sleep(0.8)

    p.ChangeFrequency(scale[2])
    time.sleep(0.4)
    p.ChangeFrequency(scale[3])
    time.sleep(0.4)
    p.ChangeFrequency(scale[4])
    time.sleep(0.4)

    p.ChangeFrequency(down_scale[4])
    time.sleep(0.4)
    p.ChangeFrequency(down_scale[5])
    time.sleep(0.4)
    p.ChangeFrequency(down_scale[6])
    time.sleep(0.4)
    p.ChangeFrequency(scale[0])
    time.sleep(0.4)
    p.ChangeFrequency(scale[1])
    time.sleep(0.4)
    p.ChangeFrequency(scale[2])
    time.sleep(0.4)
    p.ChangeFrequency(scale[3])
    time.sleep(0.4)
p.stop()                # stop the PWM output
GPIO.cleanup()
