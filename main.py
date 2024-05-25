#!/usr/bin/env python

import requests
import json
import sys
import os
import nmap
import socket 


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

def ipgeo ():
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



def menu():
    print("__________________________")
    print("1.Geo Location")
    print("2.Nmap")
    what_program = input("Enter a number of program: ")
    if what_program == "1":
        ipgeo()
    elif what_program == "2":
        nmap()
    else:
        print("error")

menu()

def loop():

    print("__________________________")
    x = int(input("0 -  Back/ 1 - Continue: "))
    if x == 0:
        menu()
    elif x == 1:
        ipgeo()
    else:
        print("error")

while True:
    loop()
