from branca.element import Html
from numpy import save
import phonenumbers
number="+91 7980154575"
import folium

from phonenumbers import geocoder
key="fb24185d56b04c5a8cfd1f70e8e2e47c"
my_number =phonenumbers.parse(number)
yourlocation=geocoder.description_for_number(my_number,'en')
print(yourlocation)
#service provider
from phonenumbers import carrier
service_provider=phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,'en'))
from opencage.geocoder import OpenCageGeocode
geocoder=OpenCageGeocode(key)
query=str(yourlocation)
result=geocoder.geocode(query)
#print(result)
lat=result[0]['geometry']['lat']
lng=result[0]['geometry']['lng']
print(lat,lng)
MyMap=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=yourlocation).add_to((MyMap))
MyMap.save("MyLOcation.html")
