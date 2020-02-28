import pandas as pd
import numpy as np
from random import randint
from .utils import dmini, dmaxi, dmean, Generator

"""
    Medium Generator, generates data according to percentage tolerance 
    of mean values of data.
    Example of sample dataset (Subject1_2D) : 

    Get every electrodes min, max and mean values. 
    Calculate the percentage of distance between mean to min and mean to max values.
    
    Then generate random numbers the range of percentage,
    according to generated percentage of each electrode calculate 
    the new distance and add or subtract with mean value.
"""
class MediumGenerator(Generator):

    def __init__(self, data):
        super().__init__(data)

        # Create empty percentages for calculations
        self.percentages = []
        self.ndata = []

        # Initializa data properties
        # Throw errors if they are not equal.
        self.arr_mini = dmini(data)
        self.arr_maxi = dmaxi(data)
        self.arr_meani = dmean(data)


    def _calc_percentage(self):

        percentages = []
        
        for mini, meani, maxi in zip(self.arr_mini, self.arr_meani, self.arr_maxi):
            dist_mini = abs(meani - mini)
            dist_maxi = abs(meani - maxi)

            minimum_distance = min(dist_mini, dist_maxi)

            percentage = (minimum_distance / meani * 100)
            percentages.append(percentage)

        return percentages
        

    # @Override method.
    def generate(self, datalen):

        self.percentages = self._calc_percentage()

        for _ in range(datalen):
            tmp_features = []
            for fi in range(len(self.features)):
                
                tpint = int(self.percentages[fi])
                rand_num = randint(min(tpint, (tpint*-1)), max(tpint, (tpint*-1)))
                val = self.arr_meani[fi] + (self.arr_meani[fi] * rand_num / 100)
                tmp_features.append(val)

            self.ndata.append(tmp_features)


        return self.ndata


