import time
import os
import sys

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
        while True:
            atbilde = input("Ievadi atbildi: ").casefold()
            if atbilde in ["a", "b", "c", "d"]:
                break
            else:
                print("Atbildi ar A, B, C vai D!")
        print()
        if atbilde == jautajums["atbilde"].casefold():
            pareizi += 1
            os.system('cls')
        else:
            nepareizi.append(jautajums)
            os.system('cls')
    print(f"Tu atbildēji uz {pareizi} jautājumiem pareizi no 10!")
    if nepareizi:
        print("Nepareizās atbildes:")
        print("-----------------------------------------------")
        for jautajums in nepareizi:
            print(jautajums["jautajums"])
            print()
            for opcija in jautajums["opcijas"]:
                print(opcija)
            print("-----------------------------------------------")
    else:
        print("Visas atbildes ir pareizas! Apsveicu!")
    while True:
        velreiz = input("Vai vēlies darīt testu atkārtoti? (jā/nē): ")
        if velreiz == 'jā':
            Sakums()
            os.system('clear')
        elif velreiz == 'nē':
            sys.exit()
        else:
            velreiz = input("Lūdzu, atbildi ar 'jā' vai 'nē': ")


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
