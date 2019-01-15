#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
Programme classique lecture entr�e GPIO avec la biblioth�que RPi.GPIO
utilisation de la fonction GPIO.input()
Bouton poussoir raccord� entre GPIO22 et +3.3V
(avec r�sistance de protection de 1k en s�rie)
nom programme       : push01.py
logiciel            : python 3.4.2
cible               : raspberry Pi
date de cr�ation    : 18/08/2016
date de mise � jour : 18/08/2016
version             : 1.0
auteur              : icarePetibles
r�f�rence           :
"""
# -------------------------------------------------------------------------------
# Biblioth�ques
# -------------------------------------------------------------------------------
import RPi.GPIO as GPIO  # biblioth�que RPi.GPIO
import time  # biblioth�que time
import pygame
# -------------------------------------------------------------------------------
green_button= 21
white_button= 26
yellow_button= 13# broche utilis� en entr�e
# temps = 1                              #valeur attente en msec
# temps = 10
temps = 100
# temps = 100
# temps = 1000

GPIO.setwarnings(False)  # d�sactive le mode warning
GPIO.setmode(GPIO.BCM)  # utilisation des num�ros de ports du
# processeur
GPIO.setup(yellow_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(white_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(green_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# mise en entr�e du port GPIO 22
# et activation r�sistance soutirage
# au ground
if __name__ == '__main__':
    """
    Programme par d�faut
    """
    Pause = false
    print("D�but du programme")  # IHM
    print("Sortie par ctrl-c\n")  # IHM
    try:
        while True:  # boucle infinie
            entree1 = GPIO.input(yellow_button)
            entree2 = GPIO.input(white_button)
            entree3 = GPIO.input(green_button)# lecture entr�e
            if (entree1 == True):  # si touche appuy�e
                print("BP jaune appuy�")  # IHM
                #Pause != Pause
            if (entree2 == True):  # si touche appuy�e
                print("BP white appuy�")  # IHM
            if (entree3 == True):  # si touche appuy�e
                print("BP green appuy�")  # IHM
            time.sleep(10)  # attente en msec
    except KeyboardInterrupt:  # sortie boucle par ctrl-c
        GPIO.cleanup()  # lib�re toutes les ressources
      