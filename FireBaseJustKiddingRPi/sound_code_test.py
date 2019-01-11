import pygame
import time
import random

#variable des playlists
playlistePirate = ["Pirate/pirate1.wav"]
playlisteComte = ["Contes/cowboy1.wav"]
playlisteFable = ["Fables/fable1.wav","Fables/fable2.wav"]


def lanceTitre(file):
    music.load(file)
    music.play()
    # le while est necessaire pour permettre la lecturebout du fichier
    while pygame.mixer.music.get_busy():
        time.sleep(1)

#POUR FAIRE DES PAUSES
        # music.pause()
        # time.sleep(5)
        # music.unpause()

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

if __name__ == "__main__":

    # initialize pygame for the sound
    mix = pygame.mixer
    music = mix.music
    mix.init()

    ButtonHistoire = True #interrupt maybe

    #introduction file with Chalut and culture point
    lanceTitre('introduction.wav')

    if ButtonHistoire:
        lancementTheme('Conte')
        lancementTheme('Fable')
        lancementTheme('Pirate')
        lanceTitre('catSounds/cat1.wav')

