class jautajumi: 
    def __init__(self, jautajums, opcijas, atbilde):
        self.jautajums = jautajums;
        self.opcijas = opcijas;
        self.atbilde = atbilde;

    def parbaudaAtbildi(self, atbile):
        return atbile == self.atbilde