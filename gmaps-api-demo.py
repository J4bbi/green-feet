import googlemaps
from datetime import datetime
import os
API_KEY = os.environ['API_KEY']
print(API_KEY)

gmaps = googlemaps.Client(key=API_KEY)
home = "EH12 6JQ, Edinburgh, UK"
work = "Royal Infirmary of Edinburgh, 51 Little France Cres, Edinburgh EH16 4SA"
modes = ["bicycling","transit", "walking", "driving"]
times = {}
distances = {}

# Request directions via public transit
now = datetime.now()

for m in modes:
    route = gmaps.directions(home, work, mode=m, departure_time=now)
    times[m] = route[0]['legs'][0]['duration']['text']
    distances[m] = route[0]['legs'][0]['distance']['text']
    print(m + ' time: ' + times[m] + '\tdistance: ' + distances[m] )
