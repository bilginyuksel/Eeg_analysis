import pandas as pd
import numpy as np
import sys
from random import randint, uniform
# Maybe import just mean
# sys.path.append(".")
from .utils import Generator, dmini, dmaxi, dmean, percentages2B
from .algorithms import findOptimumDataByProbsAndByIndex
from .constants import *
import matplotlib.pyplot as plt


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

        # assert type(self.model) == "logistic Reg", "Bla "
        self.model = model



    def configure(self):
        # print("Len Data: %s" % len(self.data))
        assert self.data is not None, "Data should not be None"
        assert self.model is not None, "You have to set model first!"
        # assert type(self.model)
            
        self._config3M()
        self._configOptimum()
        self._configPercentages()


    def _config3M(self):
        self.arr_maxi = dmaxi(self.data)
        self.arr_mini = dmini(self.data)
        self.arr_mean = dmean(self.data)

    def _configOptimum(self):
        probs = self.model.predict_proba(self.data)
        data_index, data_prob, maxfdist = findOptimumDataByProbsAndByIndex(probs, self.selected_index)
        print("\n\tData Index: %s,\n\tData Prob: %s,\n\tMaxfdist: %s" % (data_index, data_prob, maxfdist))
        self.optimum_data = self.data.loc[data_index]
        # print("Self Optimum Data: \n%s\n" % self.optimum_data)
        # print("Mean Data: \n%s\n" % self.data.mean())
        # print("Max Data: \n%s\n" % self.data.max())
        # print("Min Data: \n%s\n" % self.data.min())

    def _configPercentages(self):
        self.percentages = percentages2B(self.data.min(),self.optimum_data, self.data.max())
        print('\n\tPercentages:',self.percentages)

    # @Override method
    def generate(self, datalen):
        """
        Create random numbers between the percentages range 
        then add those percentages to optimum data..
        """
        for _ in range(datalen):
            tmp_features = []
            for j in range(len(self.features)):
                
                """
                I divided min percentage and max percentage by 2 
                because the average score was %65 and when i divided min and max by 2
                the score increased %86. 

                The thing that i did is primitive approach of normalization.
                We can evaluate this normalization method.

                --------------------------------------------------------
                BUILD A BETTER NORMALIZATON METHOD
                --------------------------------------------------------
                
                """
                min_percentage = min(self.percentages[j]*-1, self.percentages[j]) /1.5
                max_percentage = max(self.percentages[j]*-1, self.percentages[j]) /1.5
                # print("Iteration: %d,\n\tMin Percentage: %s,\n\tMax Percentage: %s" % (j, min_percentage, max_percentage))

                rand_value = uniform(min_percentage, max_percentage)
                value = self.optimum_data[j] + (self.optimum_data[j] * rand_value / 100)
                # tmp_features.append(self.optimum_data[j])
                tmp_features.append(value)

            self.ndata.append(tmp_features)

        return self.ndata


from scipy.io import loadmat
import pickle


logreg = pickle.load(open('C:/Users/bilgi/Documents/Yuksel Documents/BCI/BCI/Eeg_analysis/simulation/Logistic Regression.sav','rb'))
data = pd.DataFrame(loadmat('C:/Users/bilgi/Documents/Yuksel Documents/BCI/BCI/Eeg_analysis/tests/Subject1_2D.mat')['LeftBackward1'])

exp = ExpertGenerator(data, proba_indexes[l_forward])
exp.setModel(logreg)
exp.configure()
ndata = exp.generate(100)
print("\nData:",ndata)
result = logreg.score(ndata, ['LeftBackward' for _ in range(100)])
print("\n\tResult:",result)
# gen = ExpertGenerator(data, 0)
# gen.setModel(logreg)
# print(gen.findOptimumData())
# a, b = gen.findOptimumData()
# print(max(b))