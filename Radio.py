import numpy as np

from Mod import Mod
from Demod import Demod


#this class simulates radio transmission


class Radio:

    def __init__(self,x,s,fb, fc):
        self.input = x
        self.scheme = s
        self.fb = fb
        self.fc = fc
        
        self.mod = np.zeros(len(self.input))
        self.output = np.zeros(len(self.input))

    def modulate(self):
        #modulate input signal to prepare for transmission
        modulator = Mod(self.input,self.fb, self.fc)
        self.mod = modulator.apply(self.scheme,4)
        return self.mod

    def demodulate(self):
        #demodulate signal after transmitting through channel
        self.output = Demod.apply(self.mod)
        return self.output

    def channel(self, snr):
        #model physical constraints of a channel such as delay/distortion
        
        #Additive White Gaussian Noise (AWGN channel)
        
        #Linear Power of Noise 
        pn = 1/snr 
        noise = np.sqrt(pn/2)*np.random.randn(len(self.mod))
        rec_sig = self.mod + noise
        return rec_sig

       

if __name__ == "__main__":
    #we may compute performance here
    input = np.random.randint(2, size=16)
    #input = [1,0,1,0,1,0,1,0]
    scheme = 1
    #Radio(x, mod_scheme, bits/s, carrier frequency)
    radio = Radio(input,scheme,8, 32)
    y = radio.modulate()

    #SNR_min = 1
    #SNR_max = 9
    snr = 1
    sig = radio.channel(snr)

    demod_sig = radio.demodulate()
    #compute error between input & output


