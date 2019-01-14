from gpiozero import Button
import pygame
from time import sleep

jelly_baby = Button(3) #GPIO 3

pygame.init()
pygame.mixer.init()

burp = pygame.mixer.Sound("introduction.wav")

while True:
  jelly_baby.wait_for_press() #WAIT for the button to be pressed to start
  burp.play()
  sleep(2)
  burp.stop()
