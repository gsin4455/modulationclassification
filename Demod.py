import numpy as np

#this class simulates demodulation

class Demod:

    def __init__(self,x):
        #put parameters implicity needed for estimating the modulation scheme here
        self.input = x
        #vector of unknowns: [omegac, symbols, phasec, etc.]
        self.u = np.zeros(5)
        self.output = np.zeros(len(x))

    def mpsk(self,m):
        return self.output

    def qamm(self,m):
        return self.output

    def mask(self,m):
        return self.output

    def schema(self, scheme,m):
        schema = {
            0 : self.mpsk(m),
            1 : self.qamm(m),
            2 : self.mask(m),
        } 
        func=schema.get(scheme)
        return func()

    def classify(self):
        #implement classification algorithm here

        scheme = 0
        m=0
        return [scheme,m]
    
    def apply(self):
        #get some demodulated output after first preprocessing
        #classifier outputs modulation format
        [scheme,m] = self.classify()
        
        self.output = self.schema(scheme,m)

        return self.output

