import pandas as pd
import numpy as np
from random import randint
from .utils import Generator, dmini, dmaxi

"""
    Basic generator, generates data between min max valeus.
    Example of sample dataset (Subject1_2D) :

    There is 19 features exists in that dataset. 
    Every feature(number) represents an electrode (F1, F2, Fp1 etc.)

    Get every electrodes min and max values. And generate random numbers between that range
    for each electrode. And merge 19 new random numbers.
"""
class BasicGenerator(Generator):

    def __init__(self, data):
        super().__init__(data)

        self.ndata = []

        self.arr_maxi = ()
        self.arr_mini = ()

    def configure(self):
        self.arr_mini = dmini(self.data)
        self.arr_maxi = dmaxi(self.data)

    
    # @Override method
    def generate(self, datalen):
        for data in range(datalen):
            ftemp = []
            for feature in range(len(self.features)):
                ftemp.append(randint(int(self.arr_mini[feature]), int(self.arr_maxi[feature])))
            self.ndata.append(ftemp)

        # self.ndata = [[randint(int(self.arr_mini[feature]), int(self.arr_maxi[feature])) for feature in range(len(self.features))] for data in range(datalen)]
        return self.ndata


    

