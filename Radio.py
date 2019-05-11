import numpy as np

from Mod import Mod
from Demod import Demod


#this class simulates radio transmission


class Radio:

    def __init__(self,x,s):
        self.input = x
        self.scheme = s
        self.mod = np.zeros(self.input.shape)
        self.output = np.zeros(self.input.shape)

    def modulate(self):
        #modulate input signal to prepare for transmission
        modulator = Mod(self.input)
        self.mod = modulator.apply(self.scheme)
        return self.mod

    def demodulate(self):
        #demodulate signal after transmitting through channel
        self.output = Demod.apply(self.mod)
        return self.output

    def channel(self):
        #model physical constraints of a channel such as delay/distortion
        #add random noise etc. perhaps
        noise = np.random.rand(self.input.length())
        rec_sig = self.mod + noise
        return rec_sig

if __name__ == "__main__":
    #we may compute performance here
    input = np.random.randint(2, size=256)
    scheme = 0 
    radio = Radio(input,scheme)
    y = radio.modulate()
    print y
    #sig = radio.channel()
    #demod_sig = radio.demodulate()
    #compute error between input & output


