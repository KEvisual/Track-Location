import phonenumbers
import opencage
import folium
from myphone import number

from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)
localtion = geocoder.description_for_number(pepnumber, "en")
print(localtion)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import OpenCageGeocode

key = 'dc6527bfbd6a4dc48ffd31d169164cdc'

geocoder = OpenCageGeocode(key)
query = str(localtion)
results = geocoder.geocode(query)
#print(results)

lat = results[0] ['geometry'] ['lat']
lng = results[0] ['geometry'] ['lng']

print(lat, lng)

myMap = folium.Map(localtion= [lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=localtion).add_to(myMap) 

myMap.save("Name_file.html")