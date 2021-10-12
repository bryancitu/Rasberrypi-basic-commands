import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
pin = 4

# Agregar un evento, sin callback
GPIO.add_event_detect(pin, GPIO.BOTH)

# Comprobacion del evento
if GPIO.event_detected(pin):
    pass

# Detiene el programa hasta que ocurra el evento
GPIO.wait_for_edge(pin, GPIO.RISING, timeout=1000)