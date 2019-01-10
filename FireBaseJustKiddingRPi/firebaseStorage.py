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

jsonobj = [ {
            'Activity_Date': str(date),
            'Activity_Name': "Histoire",
            'Activity_Theme': "Cowboy",
            'Activity_Pourcentage': 80
        },
        {
            'Activity_Date': "2019-01-09 15:47:08",
            'Activity_Name': "Histoire",
            'Activity_Theme': "Cowboy",
            'Activity_Pourcentage': 80
        }
]
s = json.dumps(jsonobj)
jdata = json.loads(s)
doc_ref.set({
    u'Activities': jdata,
})

jsonobj.append( {
            'Activity_Date': "2019-01-09 15:47:08",
            'Activity_Name': "Histoire",
            'Activity_Theme': "Cowboy",
            'Activity_Pourcentage': 80
        })

s = json.dumps(jsonobj)
jdata = json.loads(s)
doc_ref.set({
    u'Activities': jdata,
})