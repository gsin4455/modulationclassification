from __future__ import division

import numpy as np
import scipy
import matplotlib.pylab as plt
import random

#this class simulates modulation

class Mod:

    def __init__(self,x): 
        #put parameters needed for the modulation scheme here
        self.input = x
        self.omegac= 2*np.pi*20000 
        self.output = np.zeros(len(self.input),dtype=float)

    def bpsk(self):

        #modulates signal using binary phase shift keying (i.e sampling 1 bit at a time)
        #transmitted signal
        x = self.input
        t = np.where(x==0, -1, 1)

        return t

    def qam4(self):

        #quadrature amplitude modulation; x = 4
        x = self.input
        #t = np.zeros(len(x),dtype=complex)


        a = np.power(-1, x[0::2])
        b = np.power(-1, x[1::2])
        t = a + b*1j
        
        return t
      
    def qam16(self):
        #00 -> 2, 01 -> 1, 10 -> -1, 11 -> -2  
        #i.e. 4x4 constellation diagram  
        #quadrature amplitude modulation; x = 16
        x = self.input

        a = np.power((-1),x[0::4])*(np.abs(np.power((-1),x[0::4]) + np.power((-1),x[1::4]))) 
        b = np.power((-1),x[2::4])*(np.abs(np.power((-1),x[2::4]) + np.power((-1),x[3::4])))
        t = a + b*1j
    
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
        nsamples = 2048
        t = np.linspace(0, 5, nsamples)
        
        sample_bit = nsamples/len(y)
        print sample_bit 
        yr = np.repeat(y, sample_bit)
        w = np.cos(self.omegac*t)*yr 

        f,ax = plt.subplots(4,1, sharex=True, sharey=True, squeeze=True)
        ax[0].plot(t, w)
        ax[0].axis([0, 0.2, -1.5, 1.5])
        ax[1].plot(t, yr)
        plt.show()
        
        #modify this to analog equivalent- multiply by carrier wave
        self.output = w
        return self.output         



if __name__ == "__main__":
#we may compute performance here
    input = np.random.randint(2, size=64)
    scheme = 0

    modulator = Mod(input)
    output = modulator.apply(scheme)
    print output



        

