Running vacationing-salesman

On the CLI:
  $: pip install geopy
  $: python3 vacationing-salesman.py cities.txt
for the basic version.

I chose python because it's what I know how to use python and there's an easy
geolocation library in python (geopy). It's also pretty easy to write clear code
with python and allows me to focus on other design decisions. I was also running
out of time because there was a protest in Berkeley, so I wasn't able to get
started early enough.

I have no idea what to do in event that it is not successful. There needs to be
at the very least, a destination and a start point to even have a salesman
traveling at all! As for the fact that if a location is the same, I'll just
assume that they meant to stay in the same city.