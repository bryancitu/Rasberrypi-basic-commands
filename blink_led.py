import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
#GPIO.setmode(GPIO.BOARD)

mode = GPIO.getmode()

print(mode)

pin = 17

GPIO.setup(pin,GPIO.OUT)


while 1:
    GPIO.output(pin, GPIO.HIGH)
    print("Encencido")
    time.sleep(1)
    GPIO.output(pin, GPIO.LOW)
    print("Apagado")
    time.sleep(1)

# Detalles adicionales
# GPIO.setup(pin, tipo, initial=1) Configurar Pin GPIO
# GPIO.input(pin) Leer un Pin GPIO

# GPIO.setwarnings(False) Desactivar o activar las alertas
# GPIO.cleanup() Restablecer los pines GPIO
# GPIO.cleanup([pin1,pin2,......])
# funcion = GPIO.gpio_funcion(pin)  Obtener la funcion del pin GPIO