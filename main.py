#!/usr/bin/env python

import requests
import json
import os 

os.system('cls' if os.name == 'nt' else 'clear')

ascii_art = """
  _____ _____     _____            _                 _   _             
 |_   _|  __ \\   / ____|          | |               | | (_)            
   | | | |__) | | |  __  ___  ___ | | ___   ___ __ _| |_ _  ___  _ __  
   | | |  ___/  | | |_ |/ _ \\/ _ \\| |/ _ \\ / __/ _` | __| |/ _ \\| '_ \\ 
  _| |_| |      | |__| |  __/ (_) | | (_) | (_| (_| | |_| | (_) | | | |
 |_____|_|       \\_____|\\___|\\___/|_|\\___/ \\___\\__,_|\\__|_|\\___/|_| |_|
                                                                       
"""

print(ascii_art)

def program ():
    
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

program()


print('----------------------------------')
x = int(input('Quit(0)/Start Again(1)'))
print('----------------------------------')
while x != 0:
    
    if x == 1:
        program()
    elif x == 0:
        sys.exit()
    else:
        x = input(str("Quit(0)/Start(1)"))




