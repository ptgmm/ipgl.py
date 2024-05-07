#!/usr/bin/env python

import requests
import json

ip = input('Enter IP Addres: ')
url = requests.get(f'https://ipinfo.io/{ip}')

output = json.loads(url.text)

hostname = (output['hostname'])
country = (output['country'])
region = (output['region'])
city = (output['city'])
loc = (output['loc'])
timezone = (output['timezone'])
postal = (output['postal'])

print(f'Hostname: {hostname}')
print(f'Country: {country}')
print(f'Region: {region}')
print(f'City: {city}')
print(f'Coordinates: {loc}')
print(f'Timezone {timezone}')
print(f'Postal: {postal}')

split = loc.split(',')
print(f'Google Maps: https://www.google.com/maps/?q={split[0]},{split[1]}')
