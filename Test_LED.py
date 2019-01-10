import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

RED = 25
GREEN = 24
BLUE = 23

GPIO.setup(RED,GPIO.OUT)
GPIO.output(RED,0)
GPIO.setup(GREEN,GPIO.OUT)
GPIO.output(GREEN,0)
GPIO.setup(BLUE,GPIO.OUT)
GPIO.output(BLUE,0)

try:
    while (True):
        GPIO.output(RED,0)
        GPIO.output(GREEN,0)
        GPIO.output(BLUE,1)
        time.sleep(2)
        
        GPIO.output(RED,0)
        GPIO.output(GREEN,1)
        GPIO.output(BLUE,0)
        time.sleep(2)
        
        GPIO.output(RED,1)
        GPIO.output(GREEN,0)
        GPIO.output(BLUE,0)
        time.sleep(2)
        
        GPIO.output(RED,1)
        GPIO.output(GREEN,0)
        GPIO.output(BLUE,1)
        time.sleep(2)
        
        GPIO.output(RED,1)
        GPIO.output(GREEN,1)
        GPIO.output(BLUE,0)
        time.sleep(2)
        
        GPIO.output(RED,0)
        GPIO.output(GREEN,1)
        GPIO.output(BLUE,1)
        time.sleep(2)
        
        GPIO.output(RED,1)
        GPIO.output(GREEN,1)
        GPIO.output(BLUE,1)
        time.sleep(2)

except KeyboardInterrupt:
        GPIO.cleanup()
