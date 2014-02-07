import requests
import json
print """
1. Almeria
2. Cadiz
3. Cordoba
4. Granada
5. Huelva
6. Jaen
7. Malaga
8. Sevilla
"""
provincias = {1:'Almeria',2:'Cadiz',3:'Cordoba',4:'Granada',5:'Huelva',6:'Jaen',7:'Malaga',8:'Sevilla'}
temp1 = int(raw_input("de que ciudad quieres saber la temperatura actual?"))
req = requests.get("http://api.openweathermap.org/data/2.5/weather", params={'q':'%s,spain'%provincias[temp1]})
dato = json.loads(req.text)
temperatura = dato['main']['temp']-273
print "la temperatura actual de",provincias[temp1], "es:",temperatura, "grados centigrados"

