import numpy as np

#this class simulates modulation

class Mod:
    def __init__(self,x,s):
        #put parameters needed for the modulation scheme here
        self.input = x
        self.omegac= 2000 #TODO: check this: carrier frequency/baseband? difference?
        self.output = np.zeros(self.input.shape)

    def bpsk(self):
        #modulates signal using binary phase shift keying (i.e sampling 1 bit at a time)
        #transmitted signal
        t = np.zeros(self.input.shape)
        x = self.input
        for i in range(0, x.length()):
            if (x[i] == 0):
                t[i] = -np.sin(self.omegac*i) #phase = -pi/2
            else:
                t[i] = np.sin(self.omegac*i) #phase = pi/2

        #note: Q[i]  = 0, I[i] = (+/-) 1 
        # -> t[i] = (+/-)j if mapped on a constellation diagram
        self.output = t
        return self.output

    def qam4(self):
        #quadrature amplitude modulation; x = 4
        t = np.zeros(self.input.shape)
        x = self.input
        for i in range(0,(x.length()/4)):
            t[(4*i):(4*i+1)] = 1 #set properly 
            t[(4*i+2) : (4*i+3)] = 0 
            
        return self.output

    def qam16(self):
        #quadrature amplitude modulation; x = 16

        return self.output

    def schema(self, scheme):
        schema = {
            0 : self.bpsk(),
            1 : self.qam4(),
            2 : self.qam16(),
        } 
        func=schema.get(scheme)
        return func()

    def apply(self,scheme):
        #apply scheme to input to get some modulated output
        self.output = self.schema(scheme)
        return self.output