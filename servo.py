
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) #Broadcom SOC channel plutot que la Board
GPIO.setup(17, GPIO.OUT) #init du PIN 11, correspondant au GPIO 17
GPIO.setwarnings(False)


pwm = GPIO.PWM(17,50) #pin et frequence (50Hz donc periode de 20ms)
periode = 20 
pwm.start(2) #duty cycle (mets a 0 degree, a tester)

        #equation pour duty cycle : (periode_angle/periode_max)*100   a tester
#tout a gauche : 2 * 100      a mesurer pour notre servo
#tout a droite : 12 * 100
#  donc equation : DutyCycle = 1/18 * (DesiredAngle) + 2

DesiredAngle = 0   #depart a 0 degree (long du corps)
DutyCycle = float(1/18 * (DesiredAngle) + 2)
pwm.ChangeDutyCycle(DutyCycle)  
time.sleep(0.8)

DesiredAngle = 135   #bras en haut : 135 degree
DutyCycle = float(1/18 * (DesiredAngle) + 2)
pwm.ChangeDutyCycle(DutyCycle)  
time.sleep(2)

DesiredAngle = 45   #bras en bas : 45 degree
DutyCycle = float(1/18 * (DesiredAngle) + 2)
pwm.ChangeDutyCycle(DutyCycle)
time.sleep(2)
     

GPIO.cleanup()

