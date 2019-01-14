import RPi.GPIO as GPIO
import pygame
import time
import random


#variable des playlists
playlistePirate = ["Pirate/pirate1.wav"]
playlisteComte = ["Contes/cowboy1.wav"]
playlisteFable = ["Fables/fable1.wav","Fables/fable2.wav"]

#GPIO.setmode(GPIO.BOARD)

#PLACE TO SET THE PIN FOR BOUTON AND HP
#GPIO.setup(21, GPIO.OUT) Bouton pour la sortie
#GPIO.setup(21, GPIO.IN) Bouton pour l'entree

def lanceTitre(file):
    music.load(file)
    music.play()
    # le while est necessaire pour permettre la lecturebout du fichier
    while pygame.mixer.music.get_busy():
        continue


def lancementTheme(nomTheme):
    if nomTheme in 'Pirate':
        i = 0
        while i < len(playlisteComte):
            random.seed(time.clock())  # for the random to be all the time different
            aleaint = random.randint(0, len(playlisteComte) - 1)
            lanceTitre(playlisteComte[aleaint])
            i+=1
    elif nomTheme in 'Fable':
        i = 0
        while i < len(playlisteFable):
            #random.seed(time.clock())  # for the random to be all the time different
            #aleaint = random.randint(0, len(playlisteFable)-1)
            lanceTitre(playlisteFable[i])
            i += 1
    else:
        i = 0
        while i < len(playlistePirate):
            random.seed(time.clock())  # for the random to be all the time different
            aleaint = random.randint(0, len(playlistePirate) - 1)
            lanceTitre(playlistePirate[aleaint])
            i += 1


while True:
    mix = pygame.mixer
    music = mix.music
    mix.init()
    Pause = False
    Stop = False
    lanceTitre('introduction.wav')

    if(GPIO.input(13) == True):  # Si le bouton histoire est appuye
        Theme = 'Pirate'
        lancementTheme('Pirate')
        if (GPIO.input(14) == True):  # si le bouton Pause est appuye
            Pause != Pause
            if (Pause):
                music.pause()
        else :
            if (GPIO.input(16) == True): # si le bouton stop est appuye
                Stop != Stop
                if (Stop):
                    music.stop()
                    if Theme == 'Pirate':
                        lancementTheme('Fable')
                    elif Theme == 'Fable':
                        lancementTheme('Conte')
                    else:
                        lancementTheme('Pirate')

