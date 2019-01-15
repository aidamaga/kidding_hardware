#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
Programme classique lecture entrée GPIO avec la bibliothèque RPi.GPIO
utilisation de la fonction GPIO.input()
Bouton poussoir raccordé entre GPIO22 et +3.3V
(avec résistance de protection de 1k en série)
nom programme       : push01.py
logiciel            : python 3.4.2
cible               : raspberry Pi
date de création    : 18/08/2016
date de mise à jour : 18/08/2016
version             : 1.0
auteur              : icarePetibles
référence           :
"""
# -------------------------------------------------------------------------------
# Bibliothèques
# -------------------------------------------------------------------------------
import RPi.GPIO as GPIO  # bibliothèque RPi.GPIO
import time  # bibliothèque time
import pygame
# -------------------------------------------------------------------------------
green_button= 21
white_button= 26
yellow_button= 13# broche utilisé en entrée
# temps = 1                              #valeur attente en msec
# temps = 10
temps = 100
# temps = 100
# temps = 1000

GPIO.setwarnings(False)  # désactive le mode warning
GPIO.setmode(GPIO.BCM)  # utilisation des numéros de ports du
# processeur
GPIO.setup(yellow_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(white_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(green_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# mise en entrée du port GPIO 22
# et activation résistance soutirage
# au ground
if __name__ == '__main__':
    """
    Programme par défaut
    """
    Pause = false
    print("Début du programme")  # IHM
    print("Sortie par ctrl-c\n")  # IHM
    try:
        while True:  # boucle infinie
            entree1 = GPIO.input(yellow_button)
            entree2 = GPIO.input(white_button)
            entree3 = GPIO.input(green_button)# lecture entrée
            if (entree1 == True):  # si touche appuyée
                print("BP jaune appuyé")  # IHM
                #Pause != Pause
            if (entree2 == True):  # si touche appuyée
                print("BP white appuyé")  # IHM
            if (entree3 == True):  # si touche appuyée
                print("BP green appuyé")  # IHM
            time.sleep(10)  # attente en msec
    except KeyboardInterrupt:  # sortie boucle par ctrl-c
        GPIO.cleanup()  # libère toutes les ressources
      