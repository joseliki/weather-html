import requests
import json
from jinja2 import Template
import webbrowser

def orienta_viento(o):
	if o>=337.5 and o<=360.0 or o>=0 and o<22.5:
		return "N"
	if o>=22.5 and o<=67.5:
		return "NE"
	if o>=67.5 and o<112.5:
		return "E"
	if o>=112.5 and o<157.5:
		return "SE"
	if o>=157.5 and o<202.5:
		return "S"
	if o>=202.5 and o<247.5:
		return "SE"
	if o>=247.5 and o<292.5:
		return "O"
	if o>=292.5 and o<337.5:
		return "NO"

provincias={'1':'Almeria','2':'Cadiz','3':'Cordoba','4':'Granada','5':'Huelva','6':'Jaen','7':'Malaga','8':'Sevilla'}
c=provincias.keys()
file=open("plantilla.html","r")
nuevo=open("wheather.html","w")
pagina=""
provin=[]
orient=[]
for f in c:
	response=requests.get("http://api.openweathermap.org/data/2.5/weather?",params={'q':'%s,spain' %c})
	provin.append(provincias[c])
	datos = json.loads(response.text)
	temp_max=int(datos['main']['temp_max'])-273	
	temp_min=int(datos['main']['temp_min'])-273
	velocidad_vi=int(datos['wind']['speed'])*1.60	
	viento=float(datos['wind']['deg']
	ori=orienta_viento(viento)
		
	
for t in file:
 pagina += t
miplantilla=Template(pagina)
resultado=miplantilla.render(p=provin, t0=temp_min, t1=temp_max, v=velocidad_vi, orienta=orient)
nueva.write(resultado)
webbrowser.open("wheather.html")
