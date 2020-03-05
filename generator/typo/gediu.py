import pandas as pd
import numpy as np
from random import randint
from .utils import dmini, dmaxi, dmean, Generator, percentages2B

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
        self.arr_mini = ()
        self.arr_maxi = ()
        self.arr_meani = ()

    def configure(self):
        self._configureMinMaxMean()
        self._configurePercentages()

    def _configureMinMaxMean(self):
        self.arr_maxi = dmaxi(self.data)
        self.arr_mini = dmini(self.data)
        self.arr_meani = dmean(self.data)

    def _configurePercentages(self):
        self.percentages = percentages2B(self.arr_mini, self.arr_meani, self.arr_maxi)



    # @Override method.
    def generate(self, datalen):

        for _ in range(datalen):
            tmp_features = []
            for fi in range(len(self.features)):
                
                tpint = int(self.percentages[fi])
                rand_num = randint(min(tpint, (tpint*-1)), max(tpint, (tpint*-1)))
                val = self.arr_meani[fi] + (self.arr_meani[fi] * rand_num / 100)
                tmp_features.append(val)

            self.ndata.append(tmp_features)


        return self.ndata


# from scipy.io import loadmat

# data = pd.DataFrame(loadmat('C:/Users/bilgi/Documents/Yuksel Documents/BCI/BCI/Eeg_analysis/tests/Subject1_2D.mat')['LeftBackward1'])
# medgen = MediumGenerator(data)
# medgen.configure()
# print("Min : ",medgen.arr_mini)
# print("Max : ",medgen.arr_maxi)
# print("Mean : ",medgen.arr_meani)
# print("Percentages : ", medgen.percentages)
# print(pd.DataFrame(medgen.generate(5)))


