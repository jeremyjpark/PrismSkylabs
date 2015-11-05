# script that takes in input from a file and outputs an itinerary

import sys
import readline
from geopy.geocoders import Nominatim


# Assumes that the last arg will by the filename with the cities
list_of_cities = open(sys.argv[-1])

# Adding all the cities to a list of cities to be geocached, but we need to
# strip the newline symbols as well... I miss chomp from ruby
cities, geocodes = [], []
geolocator = Nominatim()
for city in list_of_cities:
  cities += [city.rstrip('\n')]
  # Geocode a city to it's coordinates
  
  # add that city to a list of geocoordinates



