#!/usr/bin/env python

import sys
import os
import nmap
from scripts import ipgeo


os.system('cls' if os.name == 'nt' else 'clear')


ascii_art = """
 _                                  
(_)                                 
 _ _ __  _ __ ___   ___ _ __  _   _ 
| | '_ \\| '_ ` _ \\ / _ \\ '_ \\| | | |
| | |_) | | | | | |  __/ | | | |_| |
|_| .__/|_| |_| |_|\\___|_| |_|\\__,_|
  | |                               
  |_|                               
                                                                       
"""



def menu():

    print(ascii_art)
    print("ipgeo - 1") 
    print("nmap - 2")

    menu = input("")

    if menu == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        ipgeo.program()
    elif menu == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        nmap.program()
    else:
        print("error")
menu()


sth = 1
while sth > 0:
    ipgeo.loop()




