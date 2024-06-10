import time
import os
from Noteikumi import Noteikumi

def Sakums():
    print(Noteikumi())
    while True:
        gatavs = input("Vai esi gatavs sākt testu?")
        if gatavs == 'Jā':
            print ("Sākam!")
            time.sleep(2)
            os.system('cls')
            break
        else:
            gatavs = input("Vai esi gatavs sākt testu?")

Sakums()

