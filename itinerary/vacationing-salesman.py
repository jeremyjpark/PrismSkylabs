# script that takes in input from a file and outputs an itinerary

import sys
import readline
from geopy.geocoders import Nominatim
from geopy.distance import vincenty


# Assumes that the last arg will by the filename with the cities
list_of_cities = open(sys.argv[-1])

# Adding all the cities to a list of cities to be geocached, but we need to
# strip the newline symbols as well... I miss chomp from ruby
cities, geocodes = [], []
geolocator = Nominatim()
for city in list_of_cities:
  cities += [city.rstrip('\n')]
  # Geocode a city to it's coordinates and add that city to geocodes
  geocodes += geolocator.geocode(city.rstrip('\n'))

# Final printout
if len(cities) > 1:
  total_distance = 0
  print("Success! Your vacation itinerary is:")
  for i in range(len(cities) - 1):
    # Calculations for distance and total distance
    start = geocodes[i]
    finish = geocodes[i + 1]
    distance = vincenty((start.latitude, start.longitude), (finish.latitude, finish.longitude)).miles
    total_distance += distance
    # Print statement
    print("    " + cities[i] + " -> " + cities[i + 1] + ": " + distance + " miles")

print("    Total distance covered in your trip: " + total_distance + " miles")




