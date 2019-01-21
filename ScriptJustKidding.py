import RPi.GPIO as GPIO
import pygame
import time
import random
import json
import os
import codecs
import firebase_admin
import datetime
from firebase_admin import credentials, firestore
import random as rand 
from multiprocessing import Process


#variable des playlists

playlisteTheme = [ ["Fables/fable1.wav", "Pirate/pirate1.wav", "Contes/cowboy1.wav"],["Pirate/pirate1.wav","Contes/cowboy1.wav","Pirate/pirate1.wav","Fables/fable2.wav"]]
tabTemps = []
green_button= 16
white_button= 26
yellow_button= 13# broche utilisé en entrée
red_button = 20
GPIO.setwarnings(False)  # désactive le mode warning
GPIO.setmode(GPIO.BCM)  # utilisation des numéros de ports du
# processeur
GPIO.setup(yellow_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(white_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(green_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(red_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

RED = 25
GREEN = 24
BLUE = 23

RED1 = 5
GREEN1 = 6
BLUE1 = 19

#SET THE GPIO FOR THE FIRST LED
GPIO.setup(RED,GPIO.OUT)
GPIO.output(RED,0)
GPIO.setup(GREEN,GPIO.OUT)
GPIO.output(GREEN,0)
GPIO.setup(BLUE,GPIO.OUT)
GPIO.output(BLUE,0)

#SET THE GPIO FOR THE SECOND LED
GPIO.setup(RED1,GPIO.OUT)
GPIO.output(RED1,0)
GPIO.setup(GREEN1,GPIO.OUT)
GPIO.output(GREEN1,0)
GPIO.setup(BLUE1,GPIO.OUT)
GPIO.output(BLUE1,0)

def lanceTitre(file):
    music.load(file)
    music.play()
    time.sleep(0.25) 
    
def getMAC(interface='wlan0'):
  # Return the MAC address of the specified interface
  try:
    str = open('/sys/class/net/%s/address' %interface).read()
  except:
    str = "00:00:00:00:00:00"
  return str[0:17]
  
        

            
if __name__ == '__main__':
    
    cred = credentials.Certificate("ServiceAccountKey.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    MAC_Address = getMAC()
    doc_ref = db.collection(u'Histories').document(MAC_Address)
    doc_ref2 = db.collection(u'Appetences').document(MAC_Address)
    mix = pygame.mixer
    music = mix.music
    mix.init()
    Pause = False
    Stop = True
    index = 0
    index_theme = 0
    Histoire = False
    jsonHistory = []
    jsonAppetence = []
    compteur = 0
    prog_final_animaux = 0
    prog_final_chevaliers = 0
    dataAppetence = []
    
    
    try:
        while True:  # boucle infinie
            rand.seed(time.clock())
            r = rand.randint(0,1)
            g = rand.randint(0,1)
            b = rand.randint(0,1)
            r1 = rand.randint(0,1)
            g1 = rand.randint(1,1)
            b1 = rand.randint(0,1)
            compteur = compteur + 1
            entree1 = GPIO.input(yellow_button)
            entree2 = GPIO.input(white_button)
            entree3 = GPIO.input(green_button)# lecture entrée
            entree4 = GPIO.input(red_button)
            if not entree4 : # si on appuie sur le bouton start
                if Stop == False: # on regarde si n doit couper ou lancer le jeu
                    Stop = True
                else :
                    Stop = False
                if (Stop):
                    tabTemps.append({
                                    'Activity_Theme': ActivityTheme,
                                    'Theme_Prog' : time.time() - initial_time_theme,
                                        })
                    GPIO.output(RED, 0)
                    GPIO.output(RED1, 0)
                    GPIO.output(GREEN, 0)
                    GPIO.output(GREEN1, 0)
                    GPIO.output(BLUE, 0)
                    GPIO.output(BLUE1, 0)
                    On_Start = time.time() - initial_time #depuis cb de temps le jouet est allumé
                    print(On_Start)
                    print(time.asctime(time.localtime(On_Start)))
                    print(Stop)
                    Histoire = False
                    music.stop()
                    # Sending the History data to firebase
                    s = json.dumps(jsonHistory)
                    jdata = json.loads(s)
                    if jdata:
                       doc_ref.set({
                           u'Activities': jdata,
                        })
                       print(" sent to firebase")
                    for i in range(len(tabTemps)):
                           print (tabTemps[i])
                           
                           if tabTemps[i]['Activity_Theme'] == 'Animaux' :
                               prog_final_animaux += tabTemps[i]['Theme_Prog']
                           elif tabTemps[i]['Activity_Theme'] == 'Chevaliers' :
                               prog_final_chevaliers+= tabTemps[i]['Theme_Prog']
                    if(os.path.isfile('dataAppetence.txt')):
                        Prog_Animaux = (1-(1-(prog_final_animaux)/On_Start) * (1-float(dataAppetence[0])/100))*100
                        Prog_Chevaliers = (1-(1-(prog_final_chevaliers)/On_Start) * (1-float(dataAppetence[1])/100))*100
                    else :
                        Prog_Animaux = (prog_final_animaux*100)/On_Start
                        Prog_Chevaliers = (prog_final_chevaliers*100)/On_Start
                    jsonAppetence = {"Chansons": {
                        "Comptines": { "Image": "https://firebasestorage.googleapis.com/v0/b/justkidding-a9f10.appspot.com/o/Themes%2Ficon_comptines.png?alt=media&token=60c5e87b-058c-40c3-b629-cb5dc8b302e5",
                                        "Progression": 0
                                    }, 
                        "Disney": { "Image": "https://firebasestorage.googleapis.com/v0/b/justkidding-a9f10.appspot.com/o/Themes%2Ficon_disney.png?alt=media&token=b33c78c0-b861-44e5-bcb9-f5c31fefe8cd",
                                        "Progression": 0
                                    },
                        "Image": "https://firebasestorage.googleapis.com/v0/b/justkidding-a9f10.appspot.com/o/Themes%2Ficon_chansons.png?alt=media&token=c4c31051-5103-411d-8e37-6c7ed8c1ec88"
                                 },
                "Culture": {
                        "Aliments": { "Image": "https://firebasestorage.googleapis.com/v0/b/justkidding-a9f10.appspot.com/o/Themes%2Ficon_aliments.png?alt=media&token=cf06eacb-cbfc-4513-815f-23663038ff28",
                                        "Progression": 0
                                    },
                        "Metiers": { "Image": "https://firebasestorage.googleapis.com/v0/b/justkidding-a9f10.appspot.com/o/Themes%2Ficon_metiers.png?alt=media&token=6a4a5c83-bae5-4b32-88b2-521ca00a5eb7",
                                        "Progression": 0
                                    },
                        "Vehicules": { "Image": "https://firebasestorage.googleapis.com/v0/b/justkidding-a9f10.appspot.com/o/Themes%2Ficon_vehicules.png?alt=media&token=e10fa8ec-f615-4347-9b4b-a51a4ed1bbbc",
                                        "Progression": 0
                                    },
                        "Image": "https://firebasestorage.googleapis.com/v0/b/justkidding-a9f10.appspot.com/o/Themes%2Ficon_culture.png?alt=media&token=2cc81f7f-ca56-4721-9d53-d22f3ad7ab9c"
                         },
                "Histoires": {
                        "Animaux": { "Image": "https://firebasestorage.googleapis.com/v0/b/justkidding-a9f10.appspot.com/o/Themes%2Ficon_animaux.png?alt=media&token=c6dfa2f4-8c34-41ba-9ad9-a39056714aec",
                                        "Progression": Prog_Animaux
                                    },
                        "Chevaliers": { "Image": "https://firebasestorage.googleapis.com/v0/b/justkidding-a9f10.appspot.com/o/Themes%2Ficon_chevaliers.png?alt=media&token=495df294-5b6c-4f17-8aa5-36cdbecf33e6",
                                        "Progression": Prog_Chevaliers
                                    },
                        "Image": "https://firebasestorage.googleapis.com/v0/b/justkidding-a9f10.appspot.com/o/Themes%2Ficon_histoires.png?alt=media&token=efd6c3eb-0bbf-4ff7-b26f-5a0db9b18bd8"
                }
    }
                    s2 = json.dumps(jsonAppetence)
                    jdata2 = json.loads(s2)
                    doc_ref2.set({
                        u'Themes': jdata2,
                    })
                    # Saving the History data into the raspberry pi
                    with open('dataHistorique.txt', 'wb') as f:
                        json.dump(jdata, codecs.getwriter('utf-8')(f), ensure_ascii=False)
                        #f.close()
                    listAppetence = [Prog_Animaux, Prog_Chevaliers]
                    with open('dataAppetence.txt', 'w') as f:
                        for line in listAppetence:
                            f.write(str(line))
                            f.write("\n")
                        #f.close() 
                    print("You can restart")
                else :
                    if(os.path.isfile('dataHistorique.txt')):
                        data_historique = open('dataHistorique.txt').read()
                        jsonHistory = json.loads(data_historique)
                    if(os.path.isfile('dataAppetence.txt')):
                        with open('dataAppetence.txt', 'r') as ins:
                            for line in ins:
                                dataAppetence.append(line)
                    GPIO.output(RED, 0)
                    GPIO.output(RED1, 0)
                    GPIO.output(GREEN, 1)
                    GPIO.output(GREEN1, 1)
                    GPIO.output(BLUE, 0)
                    GPIO.output(BLUE1, 0)
                    print(Stop)
                    print("Début du programme")  # IHM
                    lanceTitre('introduction.wav')
                    
            if not entree1 and Stop == False:  # si touche appuyée
                initial_time = time.time()
                initial_time_theme = time.time()
                GPIO.output(RED, r)
                GPIO.output(RED1, r1)
                GPIO.output(GREEN, g)
                GPIO.output(GREEN1, g1)
                GPIO.output(BLUE, b)
                GPIO.output(BLUE1, b1)
                date = datetime.datetime.now()
                Histoire = True
                ActivityName = 'Histoires'
                if index_theme == 0:
                    ActivityTheme = 'Animaux'
                elif index_theme == 1:
                    ActivityTheme = 'Chevaliers'
                jsonHistory.append({
                            'Activity_Date': str(date),
                            'Activity_Name': ActivityName,
                            'Activity_Theme': ActivityTheme,
                                    })  
                lanceTitre(playlisteTheme[index_theme][index])
                index = index+1
                if index == len(playlisteTheme[index_theme]) :
                    index = 0
                    if index_theme == len(playlisteTheme):
                        #print (index_theme +" " + time.time()-initial_time)
                        index_theme = index_theme + 1 
                        GPIO.output(RED, 1)
                        GPIO.output(GREEN, 1)
                        GPIO.output(BLUE, 0)
                        GPIO.output(RED1, 0)
                        GPIO.output(GREEN1, 1)
                        GPIO.output(BLUE1, 1)
                        date = datetime.datetime.now()
                        if index_theme == 0:
                            ActivityTheme = 'Animaux'
                        elif index_theme == 1:
                            ActivityTheme = 'Chevaliers'
                        jsonHistory.append( {
                                    'Activity_Date': str(date),
                                    'Activity_Name': ActivityName,
                                'Activity_Theme': ActivityTheme,
                                })
                        tabTemps.append({
                                    'Activity_Theme': ActivityTheme,
                                    'Theme_Prog' : time.time() - initial_time_theme,
                                        })
                    
            if not pygame.mixer.music.get_busy() and Stop == False and Histoire == True :
                index = index + 1
                GPIO.output(RED, 0)
                GPIO.output(GREEN, 1)
                GPIO.output(BLUE, 1)
                GPIO.output(RED1, 1)
                GPIO.output(GREEN1, 1)
                GPIO.output(BLUE1, 0)
                lanceTitre(playlisteTheme[index_theme][index])
                        
                        
            if not entree2 and Stop == False and Histoire == True:  # si touche appuyée
                tabTemps.append({
                                    'Activity_Theme': ActivityTheme,
                                    'Theme_Prog' : time.time() - initial_time_theme,
                                        })
                index = 0
                initial_time_theme = time.time()
                index_theme = index_theme+1
                GPIO.output(RED, r)
                GPIO.output(RED1, r1)
                GPIO.output(GREEN, g)
                GPIO.output(GREEN1, g1)
                GPIO.output(BLUE, b)
                GPIO.output(BLUE1, b1)
                if index_theme == len(playlisteTheme):
                    index_theme = 0
                date = datetime.datetime.now()
                if index_theme == 0:
                    ActivityTheme = 'Animaux'
                elif index_theme == 1:
                    ActivityTheme = 'Chevaliers'
                jsonHistory.append( {
                                'Activity_Date': str(date),
                                'Activity_Name': ActivityName,
                                'Activity_Theme': ActivityTheme,
                                })
                lanceTitre(playlisteTheme[index_theme][index])
                        
            if not entree3 and Stop == False:  # si touche appuyée
                if Pause == False:
                    Pause = True
                else :
                    Pause = False
                print (Pause)
                if (Pause):
                    GPIO.output(RED, 1)
                    GPIO.output(GREEN, 1)
                    GPIO.output(BLUE, 1)
                    GPIO.output(RED1, 1)
                    GPIO.output(GREEN1, 1)
                    GPIO.output(BLUE1, 1)
                    music.pause()
                else:
                    GPIO.output(RED, 1)
                    GPIO.output(GREEN, 0)
                    GPIO.output(BLUE, 1)
                    GPIO.output(RED1, 1)
                    GPIO.output(GREEN1, 0)
                    GPIO.output(BLUE1, 1)
                    music.unpause()
        
            time.sleep(0.25)  # attente en msec
    except KeyboardInterrupt:  # sortie boucle par ctrl-c
        GPIO.cleanup()  # libère toutes les ressources



