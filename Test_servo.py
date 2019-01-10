import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(5) # Initialization
try:
  while True:                                   #mettre le cote du servo avec l'etiquette vers le haut
    p.ChangeDutyCycle(10.25)   #180 degree
    time.sleep(2)
    p.ChangeDutyCycle(5.75)     #90 degree
    time.sleep(2)
    p.ChangeDutyCycle(2.1)      #0 degree
    time.sleep(2)

    
   # p.ChangeDutyCycle(7.5)
   # time.sleep(0.5)
   # p.ChangeDutyCycle(12)
   # time.sleep(0.5)
  
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()

#GPIO.cleanup()
