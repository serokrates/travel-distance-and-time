import requests
import json
import googlemaps 
import pandas as pd
import time
import datetime
from itertools import tee
import csv
import numpy as np

time_string = "4 April, 2020, 23, 15"
result = time.strptime(time_string, "%d %B, %Y, %H, %M")
sekundy = time.mktime(result)
departure_time = sekundy

api_key ='xxxxxxxxxxxxxxxxxxxxxxxx'
gmaps = googlemaps.Client(key= api_key)


m = ['Białystok', 'Bydgoszcz', 'Gdańsk', 'Gorzów Wielkopolski', 'Katowice', 'Kielce', 'Lublin', 'Łódź', 'Olsztyn', 'Opole', 'Poznań', 'Rzeszów', 'Szczecin', 'Toruń',
 'Warszawa', 'Wrocław']

p =['Okęcie, Warszawa', 'Kraków Airport im. Jana Pawła II (KRK), Kapitana Mieczysława Medweckiego, Balice',
'Port Lotniczy Gdańsk im. Lecha Wałęsy', 'Międzynarodowy Port Lotniczy Katowice w Pyrzowicach (Katowice Airport)',
 'Port Lotniczy Wrocław S.A.', 'Mazowiecki Port Lotniczy Warszawa-Modlin',
 'Port Lotniczy Poznań-Ławica im. Henryka Wieniawskiego', 'Port Lotniczy Rzeszów-Jasionka',
  'Port Lotniczy Szczecin-Goleniów im. NSZZ Solidarność', 'Port lotniczy Lublin', 
  'Port Lotniczy Bydgoszcz S.A.', 'Port Lotniczy Łódź im. Władysława Reymonta', 
  'Port Lotniczy Olsztyn - Mazury', 'Zielona Góra Airport']

cm = len(m)
cp = len(p)
print(cm, cp)
with open('mycsv.csv', 'w', newline='') as f:
            fieldnames = ['id', 'origin', 'destination', 'duration', 'distance', 'time']
            thewriter = csv.DictWriter(f, fieldnames=fieldnames, delimiter=";")
            
            thewriter.writeheader()
            
            for x in range(0, 2):
                for y in range(0, 2):
                    
                    #print(m[x], p[y])
                    #print('dziala')
                    result = gmaps.distance_matrix(m[x],p[y],mode='driving',departure_time=sekundy)["rows"][0]["elements"][0]
                    print(result)
                    result2 = str(result)
                    bb = result2.replace("\'", "\"")
                    bb2 =bb
                    dane = json.loads(bb2)
                    thewriter.writerow({'id' : 1, 'origin' : m[x], 'destination' : p[y], 'duration' : dane['duration']['text'], 'distance': dane['distance']['text'], 'time' : time_string })

         
            
            
#print(m)
#ma = np.flipud(m)
#print(ma)
   