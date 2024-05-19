
#!/usr/bin/env python

import requests
import json
import os

def program ():
    print("__________________________")
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

def loop():
    x = input("0 - Exit/ 1 - Continue: ")
    if x == "0":
        os.system('cls' if os.name == 'nt' else 'clear')
        menu()
    elif x == "1":
        program()
    else:
        print("error")

        loop()


