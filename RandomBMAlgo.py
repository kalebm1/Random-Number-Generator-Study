"""Class for the Blum-Micali Pseudorandom Number Generation Algorithm"""
#idea: Code random n bits then convert bits to the int to return.
#Also: look into nearest prime number algo to get p...
import time
class RandomBM():
    def __init__(self,p=34319,g=4,s = 4021):
        self.p = p
        self.g = g
        self.s = s

    def getExp(self,n,p,mod):
        result = 1

        while(p):
            if(p & 1):
                result = (result*n)%mod
            n=(n*n)%mod
            p>>=1
        return result
    
    def getRandBits(self, n):
        
        a = 0
        bit = 0
        bits = ''
        i=0

        for i in range(n):
            a = self.getExp(self.g,self.s,self.p)

            if(a>(self.p-1)/2):
                bit=1
            else:
                bit=0
            bits+=str(bit)
            self.s=a
        return bits

    def setSeed(self,s):
        self.s = s
    
    def binaryToDecimal(self,bits):
        decimal = 0
        i = 0
        for i in range(len(bits)):
            bit = bits[(len(bits)-i)-1]
            val = 0
            if(bit=='0'):
                val = 0
            else:
                val=1
            decimal = decimal + val*pow(2,i)
            i+=1
        return decimal

    def getRandNumber(self):
        self.setSeed(round(time.time()*1000)%2051)
        bits = self.getRandBits(16)
        decimal = self.binaryToDecimal(bits)
        return decimal
    
    def getRandSetNum(self,a):
        self.setSeed(round(time.time()*1000)%2051)
        bits = self.getRandBits(16)
        decimal = self.binaryToDecimal(bits)
        return decimal%a


if __name__=='__main__':
    
    tester = RandomBM()
    tester.setSeed(round(time.time()*1000)%2051)
    print(tester.getRandSetNum(100))
