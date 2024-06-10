import time
import os

def Sakums ():
    while True:
        gatavs = input("Vai esi gatavs sākt testu?")

        if gatavs == 'Jā':
            print ("Sākam!")
            time.sleep(2)
            os.system('cls')
            break
        else:
            gatavs = input("Vai esi gatavs sākt testu?")

