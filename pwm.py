import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
# GPIO.setup(19, GPIO.OUT)
gpio

# PWM
pwm = GPIO.PWM(19, 2000)  # pin and frecuency
pwm.start(1)
pwm.ChangeDutyCycle(50)  # porcent of cycle

while 1:
    time.sleep(10)