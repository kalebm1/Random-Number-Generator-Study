from RandomMarsenne import Random

class WellsRandom():
    
    def __init__(self):
        self.w = 32
        self.r = 16
        self.p = 0
        self.m1 = 13
        self.m2 = 9
        self.m3 =5
        self.STATE = [0 for i in range(self.r)]
        self.state_i = 0
        self.z0 = None
        self.z1 = None
        self.z2 = None
        self.FACT = 2.32830643653869628906e-10

        self.V0 = self.STATE[self.state_i]
        self.VM1 = self.STATE[(self.state_i+self.m1) & 0x0000000F]
        self.VM2 = self.STATE[(self.state_i+self.m2) & 0x0000000F]
        self.VM3 = self.STATE[(self.state_i + self.m3)& 0x0000000F]
        self.VRm1 = self.STATE[(self.state_i+15) & 0x0000000F]
        self.VRm2 = self.STATE[(self.state_i+14) & 0x0000000F]
        self.newV0 = self.STATE[(self.state_i+15) & 0x0000000F]
        self.newV1 = self.STATE[self.state_i]
        self.newVRm1 =self.STATE[(self.state_i+14) & 0x0000000F]

    def MAT0POS(self,t,v):
        return (v^(v>>t))
    
    def MAT0NEG(self,t,v):
        return (v^(v<<(-(t))))
    
    def MAT3NEG(self,t,v):
        return (v<<(-(t)))
    
    def MAT4NEG(self,t,b,v):
        return (v^((v<<(-(t))) & b))

    def InitWELLRNG512a (self):
        j = 0
        randomdata = Random()
        self.state_i = 0
        for j in range(self.r):
            deltar = int(randomdata.randint(0,600))^(int(randomdata.randint(0,600))<<16)^(int(randomdata.randint(0,600))<<31)
            print(str(deltar))
            self.STATE[j] = deltar
    
    def WELLRNG512a(self):

        self.V0 = self.STATE[self.state_i]
        self.VM1 = self.STATE[(self.state_i+self.m1) & 0x0000000F]
        self.VM2 = self.STATE[(self.state_i+self.m2) & 0x0000000F]
        self.VM3 = self.STATE[(self.state_i + self.m3)& 0x0000000F]
        self.VRm1 = self.STATE[(self.state_i+15) & 0x0000000F]
        self.VRm2 = self.STATE[(self.state_i+14) & 0x0000000F]
        self.newV0 = self.STATE[(self.state_i+15) & 0x0000000F]
        self.newV1 = self.STATE[self.state_i]
        self.newVRm1 =self.STATE[(self.state_i+14) & 0x0000000F]




        self.z0 = self.VRm1
        self.z1 = self.MAT0NEG(-16,self.V0) ^ self.MAT0NEG(-15,self.VM1)
        self.z2 = self.MAT0POS(11,self.VM2)
        self.newV1 = self.z1^self.z2
        self.newV0 = self.MAT0NEG(-2,self.z0) ^ self.MAT0NEG(-18,self.z1) ^ self.MAT3NEG(-28,self.z2) ^ self.MAT4NEG(-5,0xda442d24,self.newV1)

        self.state_i = (self.state_i+15)&0x0000000f

        return self.STATE[self.state_i] * self.FACT
