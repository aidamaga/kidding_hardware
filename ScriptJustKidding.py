import RPi.GPIO as GPIO
import pygame
import time
import random


#variable des playlists

playlisteTheme = [ ["Fables/fable1.wav", "Pirate/pirate1.wav", "Contes/cowboy1.wav"],["Fables/fable1.wav","Contes/cowboy1.wav","Pirate/pirate1.wav","Fables/fable2.wav"]]
green_button= 16
white_button= 26
yellow_button= 13# broche utilisé en entrée

GPIO.setwarnings(False)  # désactive le mode warning
GPIO.setmode(GPIO.BCM)  # utilisation des numéros de ports du
# processeur
GPIO.setup(yellow_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(white_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(green_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# mise en entrée du port GPIO 22
# et activation résistance soutirage
# au ground
def lanceTitre(file):
    music.load(file)
    music.play()
    # le while est necessaire pour permettre la lecturebout du fichier
    #while pygame.mixer.music.get_busy():
        #continue
    time.sleep(0.25) 
    
        

            
if __name__ == '__main__':
    """
    Programme par défaut
    """
    mix = pygame.mixer
    music = mix.music
    mix.init()
    Pause = False
    print("Début du programme")  # IHM
    lanceTitre('introduction.wav')
    index = 0
    index_theme = 0
    Histoire = False
    
    try:
        while True:  # boucle infinie
            
            entree1 = GPIO.input(yellow_button)
            entree2 = GPIO.input(white_button)
            entree3 = GPIO.input(green_button)# lecture entrée
            if not entree1 :  # si touche appuyée
                Histoire = True
                print("Bouton Histoire / Next")
                lanceTitre(playlisteTheme[index_theme][index])
                print(index)
                index = index+1
                print(index)
                print("len playliste" + str(len(playlisteTheme[index_theme])))
                if index == len(playlisteTheme[index_theme]) :
                    index = 0
                    if index_theme == len(playlisteTheme):
                        index_theme = index_theme + 1 
            
            
            if not pygame.mixer.music.get_busy():
                print("Next Song")
                index = index + 1
                lanceTitre(playlisteTheme[index_theme][index])
                
                
            if not entree2 :  # si touche appuyée
                print("Bouton  change the theme")
                index = 0
                index_theme = index_theme+1
                print(index_theme)
                print("len playliste" + str(len(playlisteTheme)))
                if index_theme == len(playlisteTheme):
                    index_theme = 0
                    print(index_theme)
                    print(index)
                lanceTitre(playlisteTheme[index_theme][index])
                
            if not entree3 :  # si touche appuyée
                print("Bouton Pause / Play")  # IHM
                if Pause == False:
                    Pause = True
                else :
                    Pause = False
                print (Pause)
                if (Pause):
                    music.pause()
                else:
                    music.unpause()

            time.sleep(0.25)  # attente en msec
    except KeyboardInterrupt:  # sortie boucle par ctrl-c
        GPIO.cleanup()  # libère toutes les ressources



