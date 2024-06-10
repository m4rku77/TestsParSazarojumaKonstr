import time
import os

from Jautajumi import jautajumi
from Noteikumi import Noteikumi

def tests():
    pareizi = 0
    nepareizi = []
    for jautajums in jautajumi:
        print(jautajums["jautajums"])
        for opcija in jautajums["opcijas"]:
            print(opcija)
        print()
        atbilde = input("Ievadi atbildi: ").upper()
        print()
        if atbilde == jautajums["atbilde"]:
            pareizi += 1
            os.system('cls')
        else:
            nepareizi.append(jautajums)
            os.system('cls')
    print(f"Tu atbildēji uz {pareizi} jautājumiem pareizi no 10!")
    if nepareizi:
        print("Nepareizas atbildes:")
        print("-----------------------------------------------")
        for jautajums in nepareizi:
            print(jautajums["jautajums"])
            print()
            for opcija in jautajums["opcijas"]:
                print(opcija)
            print("-----------------------------------------------")
    else:
        print("Visas atbildes ir pareizas!")

def Sakums():
    print(Noteikumi())
    while True:
        gatavs = input("Vai esi gatavs sākt testu? ")
        if gatavs == 'jā':
            print ("Sākam!")
            time.sleep(2)
            os.system('cls')
            tests()
            break
        else:
            gatavs = input("Vai esi gatavs sākt testu?")

Sakums()
