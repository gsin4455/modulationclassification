import numpy as np
import random

#this class simulates modulation

class Mod:

    def __init__(self,x): 
        #put parameters needed for the modulation scheme here
        self.input = x
        self.omegac= 2*np.pi*2000 
        self.output = np.zeros(len(self.input),dtype=float)

    def bpsk(self):

        #modulates signal using binary phase shift keying (i.e sampling 1 bit at a time)
        #transmitted signal
        x = self.input
        t = np.zeros(len(x),dtype=complex)
        for i in range(0, len(x)):
            if (x[i] == 0):
                t[i] = -1 #phase = -pi
            else:
                t[i] = 1 #phase = pi/2
            
        #note: I[i]  = 0, Q[i] = (+/-) 1 
        # -> t[i] = (+/-)1 if mapped on a constellation diagram

        return t

    def qam4(self):

        #quadrature amplitude modulation; x = 4
        x = self.input
        t = np.zeros(len(x),dtype=complex)

        a = 0
        b = 0
        i = 0

        while i < len(x):
            #0 -> +1, 1 -> -1  
            #i.e. 00 -> (1,1), 10 -> (-1,1), 01 -> (1,-1), 11 -> (-1, -1)
            a = np.power((-1),x[i])
            b = np.power((-1),x[(i)+1])
            t[i:(i+1)] = a + b*1j
            i = i + 2
        return t

    def qam16(self):

        #quadrature amplitude modulation; x = 16
        x = self.input
        t = np.zeros(len(x), dtype=complex)
        a = 0
        b = 0
        i = 0

        while i < len(x):
            #00 -> 2, 01 -> 1, 10 -> -1, 11 -> -2  
            #i.e. 4x4 constellation diagram  
            a = np.power((-1),x[i])*(np.abs(np.power((-1),x[i]) + np.power((-1),x[i+1]))) 
            b = np.power((-1),x[i+2])*(np.abs(np.power((-1),x[i+2]) + np.power((-1),x[i+3])))
            i = i + 4
            t[i:(i+3)] = a + b*1j

        return t

    def schema(self, scheme):
        schema = {
            0 : self.bpsk,
            1 : self.qam4,
            2 : self.qam16,
        } 

        func=schema[scheme]()
        
        return func

    def apply(self,scheme):
        #apply scheme to input to get some modulated output
        y = self.schema(scheme)
        print scheme
        n = np.arange(0,len(self.input))

        #modify this to analog equivalent- multiply by carrier wave
        self.output = y*np.cos(self.omegac*n) 

        return self.output         




if __name__ == "__main__":
#we may compute performance here
    input = np.random.randint(2, size=256)
    scheme = 2

    modulator = Mod(input)
    output = modulator.apply(scheme)
    print output



        

