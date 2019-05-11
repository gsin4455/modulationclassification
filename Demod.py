import numpy as np

#this class simulates demodulation

class Demod:

    def __init__(self,x):
        #put parameters implicity needed for estimating the modulation scheme here
        self.input = x
        #vector of unknowns: [omegac, symbols, phasec, etc.]
        self.u = np.zeros(5)
        self.output = np.zeros(len(x))

    def bpsk(self):
        #binary phase shift keying        
        return self.output

    def qam4(self):
        #quadrature amplitude modulation; x = 4
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

    def classify(self):
        #implement classification algorithm here

        scheme = 0
        return scheme
    
    def apply(self):
        #get some demodulated output after first preprocessing
        #classifier outputs modulation format
        scheme = self.classify()
        self.output = self.schema(scheme)

        return self.output

