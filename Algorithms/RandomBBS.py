""" This is the class for the Blum Blum Shub Pseudorandom Number Generator """

class RandomBBS():
    def __init__(self,p=11,q=23,s=4):
        self.p = p
        self.q = q
        self.x0 = s
        self.n = p*q
    

    def getRandNumber(self):
        nextRandNum = (self.x0*self.x0)%self.n
        self.x0 = nextRandNum
        return nextRandNum

    def getRandBit(self):
        return self.getRandNumber()%2

    def setP(self,p):
        self.p = p
    
    def setQ(self,q):
        self.q = q
    
    def setSeed(self,s):
        self.x0 = s
