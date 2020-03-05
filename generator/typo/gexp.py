import pandas as pd
import numpy as np
import sys
from random import randint
# Maybe import just mean
# sys.path.append(".")
from .utils import Generator, dmini, dmaxi, dmean


"""
    Expert Generator, generates data according to best data one of its kind.

    Example of sample dataset (Subject1_2D) :
    Find the data of its best kind. 
    Find the optimum percentage of data and create data
    according to that percentage.

    Best data finding method is :: First of all import a logistic regression model
    to find classes probabilities. According to asked class, find the minimum distance 
    between classes and try to find the max distancne between those minimum distances.
"""
class ExpertGenerator(Generator):
    
    def __init__(self, data, selected_index):
        super().__init__(data)

        self.selected_index = selected_index
        self.optimum_data = []
        self.model = None

        self.percentages = []
        self.ndata = []

        self.arr_mini = ()
        self.arr_maxi = ()
        self.arr_mean = ()

    def setModel(self, model):
        self.model = model

    def configure(self):
        self._config3M()
        self._configOptimum()
        self._configPercentages()


    def _config3M(self):
        self.arr_maxi = dmaxi(self.data)
        self.arr_mini = dmini(self.data)
        self.arr_mean = dmean(self.data)

    def _configOptimum(self):
        pass

    def _configPercentages(self):
        pass

    def _findDist(self, data1, data2):
        return abs(data1 - data2)

    def findOptimumData(self, category_index = 1):
        # Get probabalities of model
        res = self.model.predict_proba(self.data)

        # Declare which data to search
        # res1 = self.model.predict(self.data[:100])

        general_index = 0
        for i in res:
            # it traverses a list
            # which one we are trying to search
            maxfdist = 0
            # Declare fdist first
            fdist = self._findDist(i[self.selected_index], i[0])

            for j in range(len(i)):
                # Find the minimum distance between class probabilities
                if self._findDist(i[self.selected_index], i[j]) < fdist:
                    fdist = self._findDist(i[self.selected_index], i[j])

            # Find the maximum distance among minimum distances.
            if maxfdist < fdist:
                maxfdist = fdist
                general_index = i

        # return the index of the data which is best of its kind
        return self.data.loc[general_index], res[general_index]





    # @Override method
    def generate(self, datalen):
        
        self.optimum_data = self._findOptimumData()
        self.percentages = self._findPercentages()


from scipy.io import loadmat
import pickle


logreg = pickle.load(open('C:/Users/bilgi/Documents/Yuksel Documents/BCI/BCI/Eeg_analysis/simulation/Logistic Regression.sav','rb'))
data = pd.DataFrame(loadmat('C:/Users/bilgi/Documents/Yuksel Documents/BCI/BCI/Eeg_analysis/tests/Subject1_2D.mat')['LeftBackwardImagined'])
gen = ExpertGenerator(data, 0)
gen.setModel(logreg)
# print(gen.findOptimumData())
a, b = gen.findOptimumData()
print(max(b))