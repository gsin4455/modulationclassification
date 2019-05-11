import numpy as np

#this class simulates demodulation

class Demod:
    def __init__(self,x):
        #put parameters implicity needed for estimating the modulation scheme here
        self.input = x

        #vector of unknowns: [omegac, symbols, phasec, etc.]
        self.u = np.zeros(5)
        self.output = np.zeros(self.input.shape)


    def bpsk(self):
        #modulates signal using binary phase shift keying
        x = self.input
        omegac = self.u[0]
        t = np.zeros(self.input.shape)
        for i in range(0, x.length()):
            '''' -not sure about this
            if (x[i] == 0):
                t[i] = -np.sin(omegac*i) #phase = -pi/2
            else:
                t[i] = np.sin(omegac*i) #phase = pi/2

            '''
       
        self.output = t
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

