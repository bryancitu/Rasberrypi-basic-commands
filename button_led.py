import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
# Entradas

# GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(17, GPIO.IN)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)

def encender_led(pin):
    GPIO.output(6, GPIO.HIGH)
    print("Interrupcion")

def apagar_led(pin):
    GPIO.output(6, GPIO.LOW)

GPIO.add_event_detect(17, GPIO.RISING , callback = encender_led)
# GPIO.add_event_detect(4,GPIO.RISING, callback = apagar_led)

while 1:
    GPIO.output(5, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(5, GPIO.LOW)
    time.sleep(5)
    # if GPIO.input(4):
    #     GPIO.output(6, GPIO.HIGH)
    # else:
    #     GPIO.output(6,GPIO.LOW)