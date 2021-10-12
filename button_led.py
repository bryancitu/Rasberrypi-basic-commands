import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
# Entradas

# GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(17, GPIO.IN)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

GPIO.output(15, GPIO.LOW)

def encender_led(pin):
    GPIO.output(15, GPIO.HIGH)
    print("Interrupcion")

def apagar_led(pin):
    GPIO.output(15, GPIO.LOW)

GPIO.add_event_detect(17, GPIO.RISING , callback = encender_led)
# GPIO.add_event_detect(4,GPIO.RISING, callback = apagar_led)

while 1:
    GPIO.output(14, GPIO.HIGH)
    time.sleep(14)
    GPIO.output(14, GPIO.LOW)
    time.sleep(14)
    # if GPIO.input(4):
    #     GPIO.output(6, GPIO.HIGH)
    # else:
    #     GPIO.output(6,GPIO.LOW)