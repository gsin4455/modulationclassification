from __future__ import division

import numpy as np
import scipy
import matplotlib.pylab as plt
import random

from decimal import Decimal

#this class simulates modulation



class Mod:

    def __init__(self,x,fb,fc): 
        #put parameters needed for the modulation scheme here
        self.input = x
        self.fc = fc
        self.fb = fb
        self.output = np.zeros(len(self.input),dtype=float)
        self.fs = 2*self.fc
        self.sample_bit = self.fs/self.fb
        self.t =  np.linspace(0, (len(self.input)/self.fb), self.fs*(len(self.input)/self.fb))
        self.bits = []


    def BCD(self,x): 
      #Binary to Decimal converter (takes in bit sequence)
        dec, i = 0, 0
        for i in range(len(x)):
            dec = dec + int(x[i])*np.power(2,len(x)-i-1)
        return dec 

    
    def mpsk(self,m):

        #modulates signal using binary phase shift keying (i.e sampling 1 bit at a time)
        #transmitted signal
        lm = int(np.log2(m))
        x = self.input
        M = int(len(x)/lm)
        y = np.zeros(M)

        for i in range(M):
            y[i] = self.BCD(x[(lm*i):(lm*i+lm)])
        
        y = np.repeat(y, lm*self.sample_bit)
        
        s = np.cos(self.fc*self.t + 2*np.pi*(y)/(m))
        #s  = self.t
        return s

    def qamm(self,m):
        lm = int(np.log2(m))
        x = self.input
        M = int(len(x)/lm)            
        a = np.zeros(M)
        b = np.zeros(M)

        for i in range(M):
            z = x[lm*i: lm*i + lm]
            a[i] = self.BCD(z[0::2])
            b[i] = self.BCD(z[1::2])
       
        a = np.repeat(a,lm*self.sample_bit)
        b = np.repeat(b, lm*self.sample_bit) 
        s = a*np.cos(self.fc*self.t) + b*np.sin(self.fc*self.t)
        return s


    def mask(self, m):
        lm = int(np.log2(m))
        x = self.input
        M = int(len(x)/lm)
        y = np.zeros(M)

        for i in range(M):
            y[i] = self.BCD(x[(lm*i):(lm*i+lm)])

        y = np.repeat(y, lm*self.sample_bit)

        s = y*np.cos(self.fc*self.t)
        return s

    def schema(self, scheme,m):
        schema = {
            0 : self.mpsk,
            1 : self.qamm,
            2 : self.mask,
        } 

        output=schema[scheme](m)
        
        return output

    def apply(self,scheme,m):
        
        
        #apply scheme to input to get some modulated output
        y = self.schema(scheme,m)
        
        f,ax = plt.subplots(2,1, sharex=True, sharey=True, squeeze=True)
        ax[0].plot(self.t, y, dashes = [6,2])
        ax[0].axis([0, np.max(self.t),-4, 4])
        ax[1].plot(self.t, np.repeat(self.input, self.sample_bit))
            
        plt.show()
        
        self.output = y
        return self.output         



if __name__ == "__main__":
#we may compute performance here
    



        

