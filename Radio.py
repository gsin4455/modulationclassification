import numpy as np
import matplotlib.pylab as plt

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
        
        self.fs = 48*self.fc
        self.sample_bit = self.fs/self.fb
        self.t =  np.linspace(0, (len(self.input)/self.fb), self.fs*(len(self.input)/self.fb))

    def modulate(self):
        #modulate input signal to prepare for transmission
        modulator = Mod(self.input,self.fb, self.fc)
        self.mod = modulator.apply(self.scheme,2)
        return self.mod

    def demodulate(self):
        #demodulate signal after transmitting through channel
        self.output = Demod.apply(self.mod)
        return self.output

    def channel(self, snr, ct):
        '''
        Model the channel of transmission system:
            1.Additive White Gaussian Noise (AWGN channel)
            2.Fading (Flat or Frequency Selective)
            3. Non-Gaussian (optional)
        '''    


        ln = len(self.mod)
    #1.
        rec_sig = self.mod
        pn = 1.0/snr 
        awgn_noise = np.sqrt(pn/2)*np.random.randn(ln)
        
    #2.
        if (ct == 1):
            #Fading Channel
            
            amean = 0.5                      #Average attenuation 
            pmean = 10*(np.pi/180)           #Average phase offset
            avar = 0.1                       #Variance of attenuation
            pvar = 1*(np.pi/180)             #Variance of phase offset
            fo = self.fc*(5/(3*10^8))        #Frequency offset


            ao = np.random.normal(amean,avar,ln)
            po = np.random.normal(pmean,pvar,ln)

            rec_sig = ao*np.exp(1j*(2*np.pi*self.t*fo + po))*rec_sig

        rec_sig = rec_sig + awgn_noise
        return rec_sig

if __name__ == "__main__":
    #we may compute performance here
    input = np.random.randint(2, size=16)
    scheme = 0
    #Radio(x, modulation scheme, baud rate, carrier frequency)
    radio = Radio(input,scheme,8,32)
    radio.mod = radio.modulate()

    #Channel type: 0 = AWGN, 1 = (Unified) Fading
    snr = 200 #dB
    channel_type = 0
    sig = radio.channel(snr, channel_type)

    f,ax = plt.subplots(3,1, constrained_layout=True)
    ax[0].plot(radio.t,sig, dashes = [6,2])
    ax[0].axis([0, np.max(radio.t),-2*sig.max(), 2*sig.max()])
    ax[1].plot(radio.t, np.repeat(input, radio.sample_bit))
    ax[0].set_title('Modulated Wave')
    ax[1].set_title('Input')
    ax[0].set_xlabel('Time',fontsize=8 )
    ax[0].set_ylabel('Amplitude',fontsize=8)
    ax[1].set_xlabel('Time',fontsize=8)
    ax[1].set_ylabel('Amplitude',fontsize=8)
    ax[2].set_xlabel('Real',fontsize=8)
    ax[2].set_ylabel('Imaginary',fontsize=8)


    plt.show()
    

    #demod_sig = radio.demodulate()
    #compute error between input & output


