"""This is an attempt to make the Mersenne Twister Algorithm in Pyhton"""
import psutil,time


class Random():
    def __init__(self,c_seed=round((psutil.virtual_memory().total / (1024.0 **3))*(time.time()-36.7))):
        self.w = 32
        self.n = 624
        self.m = 397
        self.r = 31
        self.a = 0x9908B0DF
        self.u = 11
        self.d = 0xFFFFFFFF
        self.s = 7
        self.b = 0x9D2C5680
        self.t = 15
        self.c = 0xEFC60000
        self.l = 18
        self.f = 1812433253

        self.MT = [0 for i in range(self.n)]

        self.index = self.n+1
        self.lower_mask = 0xFFFFFFFF
        self.upper_mask = 0x00000000

        self.c_seed = c_seed
        self.seed(c_seed)
    
    def seed(self,num):
        self.index = self.n
        self.MT[0] = num

        for i in range(1, self.n):
            temp = self.f*(self.MT[i-1] ^ (self.MT[i-1] >> (self.w-2)))+i
            self.MT[i] = temp & 0xffffffff

    def twist(self):
        for i in range(0,self.n):
            x = (self.MT[i] & self.upper_mask) + (self.MT[(i+1)%self.n] & self.lower_mask)
            xA = x >> 1
            if(x%2) != 0:
                xA = xA ^ self.a
            self.MT[i] = self.MT[(i+self.m) % self.n] ^ xA
        
        self.index = 0


    def extract_number(self):
        if self.index >= self.n:
            if self.index > self.n:
                pass
            self.twist()
        
        y = self.MT[self.index]
        y = y ^ ((y >> self.u) & self.d)
        y = y ^ ((y<< self.s) & self.b)
        y = y ^ ((y<< self.t) & self.c)
        y = y ^ (y>>self.l)

        self.index = self.index+1
        return y&0xffffffff

    def random(self):

        return self.extract_number() / 4294967296

    def randint(self, a, b):
        n = self.random()
        return int(n/(1/(b-a))+a)
    
    # def randint(self):
    #     n = self.random()
    #     return(int( n/(1/(100000-0))+0))
    


# class WellsRandom():
    
#     def __init__(self):
#         self.w = 32
#         self.r = 16
#         self.p = 0
#         self.m1 = 13
#         self.m2 = 9
#         self.m3 =5
#         self.STATE = [0 for i in range(self.r)]
#         self.state_i = 0
#         self.z0 = None
#         self.z1 = None
#         self.z2 = None
#         self.FACT = 2.32830643653869628906e-10

#         self.V0 = self.STATE[self.state_i]
#         self.VM1 = self.STATE[(self.state_i+self.m1) & 0x0000000F]
#         self.VM2 = self.STATE[(self.state_i+self.m2) & 0x0000000F]
#         self.VM3 = self.STATE[(self.state_i + self.m3)& 0x0000000F]
#         self.VRm1 = self.STATE[(self.state_i+15) & 0x0000000F]
#         self.VRm2 = self.STATE[(self.state_i+14) & 0x0000000F]
#         self.newV0 = self.STATE[(self.state_i+15) & 0x0000000F]
#         self.newV1 = self.STATE[self.state_i]
#         self.newVRm1 =self.STATE[(self.state_i+14) & 0x0000000F]

#     def MAT0POS(self,t,v):
#         return (v^(v>>t))
    
#     def MAT0NEG(self,t,v):
#         return (v^(v<<(-(t))))
    
#     def MAT3NEG(self,t,v):
#         return (v<<(-(t)))
    
#     def MAT4NEG(self,t,b,v):
#         return (v^((v<<(-(t))) & b))

#     def InitWELLRNG512a (self):
#         j = 0
#         randomdata = Random(5489)
#         self.state_i = 0
#         for j in range(self.r):
#             print(str(int(randomdata.randint())^(int(randomdata.randint())<<16)^(int(randomdata.randint())<<31)))
#             self.STATE[j] = int(randomdata.randint())^(int(randomdata.randint())<<16)^(int(randomdata.randint())<<31)
    
#     def WELLRNG512a(self):

#         self.V0 = self.STATE[self.state_i]
#         self.VM1 = self.STATE[(self.state_i+self.m1) & 0x0000000F]
#         self.VM2 = self.STATE[(self.state_i+self.m2) & 0x0000000F]
#         self.VM3 = self.STATE[(self.state_i + self.m3)& 0x0000000F]
#         self.VRm1 = self.STATE[(self.state_i+15) & 0x0000000F]
#         self.VRm2 = self.STATE[(self.state_i+14) & 0x0000000F]
#         self.newV0 = self.STATE[(self.state_i+15) & 0x0000000F]
#         self.newV1 = self.STATE[self.state_i]
#         self.newVRm1 =self.STATE[(self.state_i+14) & 0x0000000F]




#         self.z0 = self.VRm1
#         self.z1 = self.MAT0NEG(-16,self.V0) ^ self.MAT0NEG(-15,self.VM1)
#         self.z2 = self.MAT0POS(11,self.VM2)
#         self.newV1 = self.z1^self.z2
#         self.newV0 = self.MAT0NEG(-2,self.z0) ^ self.MAT0NEG(-18,self.z1) ^ self.MAT3NEG(-28,self.z2) ^ self.MAT4NEG(-5,0xda442d24,self.newV1)

#         self.state_i = (self.state_i+15)&0x0000000f

#         return self.STATE[self.state_i] * self.FACT

