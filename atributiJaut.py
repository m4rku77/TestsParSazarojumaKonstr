from Jautajumi import jautajumi

class atributiJaut: 
    def __init__(self, jautajums, opcijas, atbilde):
        self.jautajums = jautajums;
        self.opcijas = opcijas;
        self.atbilde = atbilde;

    def display(self):
        print(self.jautajums)
        for i, atbilde in enumerate(self.jautajums):
            print(f"{chr(65 + i)}. {atbilde}")
        print()


    def parbaudaAtbildi(self, atbilde):
        return atbilde == self.atbilde
    

    