from __future__ import division

import numpy as np
import scipy
import matplotlib.pylab as plt
import random

#this class simulates modulation

class Mod:

    def __init__(self,x,fb,fc): 
        #put parameters needed for the modulation scheme here
        self.input = x
        self.fc = fc
        self.fb = fb
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

        output=schema[scheme]()
        
        return output

    def apply(self,scheme):

        #apply scheme to input to get some modulated output
        y = self.schema(scheme)
        
        #sampling frequency- nyquist theorem
        fs = 2*self.fc
        sample_bit = fs/self.fb
        t = np.linspace(0, (len(y)/self.fb), fs*(len(y)/self.fb))

        yr = np.repeat(y, sample_bit)

        #convolving spectrum with DFT of carrier
        w = np.cos(2*np.pi*(self.fc)*t)*yr
        
        #demodulated
        d = np.cos(2*np.pi*(self.fc)*t)*w

        f,ax = plt.subplots(4,1, sharex=True, sharey=True, squeeze=True)
        ax[0].plot(t, w)
        ax[0].axis([0, 0.1, -1.5, 1.5])
        ax[1].plot(t, yr)
        ax[2].plot(t, d)

        plt.show()
        
        self.output = w
        return self.output         



if __name__ == "__main__":
#we may compute performance here
    input = np.random.randint(2, size=128)
    scheme = 0

    #frequency of carrier
    modulator = Mod(input,128, 512)
    output = modulator.apply(scheme)
   



        

