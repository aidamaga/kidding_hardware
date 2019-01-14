import json

import firebase_admin
import datetime
from firebase_admin import credentials, firestore

def getMAC(interface='wlan0'):
  # Return the MAC address of the specified interface
  try:
    str = open('/sys/class/net/%s/address' %interface).read()
  except:
    str = "00:00:00:00:00:00"
  return str[0:17]

cred = credentials.Certificate("ServiceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
#MAC_Address = getMAC()
MAC_Address = "laVJcAzoVI9GHFS9lBWJ"
date = datetime.datetime.now()
doc_ref = db.collection(u'Histories').document(MAC_Address)

jsonHistory = [ {
            'Activity_Date': str(date),
            'Activity_Name': "Histoire",
            'Activity_Theme': "Cowboy",
        },
        {
            'Activity_Date': "2019-01-09 15:47:08",
            'Activity_Name': "Histoire",
            'Activity_Theme': "Cowboy",
        }
]
s = json.dumps(jsonHistory)
jdata = json.loads(s)
doc_ref.set({
    u'Activities': jdata,
})

jsonHistory.append( {
            'Activity_Date': "2019-01-09 15:47:08",
            'Activity_Name': "Histoire",
            'Activity_Theme': "Cowboy",
        })

s = json.dumps(jsonHistory)
jdata = json.loads(s)
doc_ref.set({
    u'Activities': jdata,
})

doc_ref = db.collection(u'Appetences').document(MAC_Address)

jsonAppetence = {"Chanson": {
                        "Comptines": 80,
                        "Disney": 50
                                 },
                "Culture": {
                        "Aliments": 20,
                        "Metiers": 10,
                        "Vehicules": 5
                         },
                "Histoires": {
                        "Animaux": 60,
                        "Chevaliers": 35
                }
    }

s2 = json.dumps(jsonAppetence)
jdata2 = json.loads(s2)
doc_ref.set({
    u'Themes': jdata2,
})