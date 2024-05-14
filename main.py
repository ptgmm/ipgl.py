#!/usr/bin/env python

import sys
import os
import nmap
import ipgeo 


os.system('cls' if os.name == 'nt' else 'clear')

ascii_art = """
 _                                  
(_)                                 
 _ _ __  _ __ ___   ___ _ __  _   _ 
| | '_ \| '_ ` _ \ / _ \ '_ \| | | |
| | |_) | | | | | |  __/ | | | |_| |
|_| .__/|_| |_| |_|\___|_| |_|\__,_|
  | |                               
  |_|                               
                                                                       
"""

print(ascii_art)

def menu():
    print("IP Geo Loacation")
    print("NMAP Port Scanner")
    
def main():
    ipgeo.program()

def loop():

    x = int(input("0 - Exit/ 1 - Continue: "))
    if x == 0:
        sys.exit()
    elif x == 1:
        program()
    else:
        print("error")

while True: 
    loop()


