import pandas as pd
import numpy as np
from random import randint
# Maybe import just mean
from .utils import Generator, dmini, dmaxi, dmean


"""
    Expert Generator, generates data according to best data one of its kind.

    Example of sample dataset (Subject1_2D) :
    Find the data of its best kind. 
    Find the optimum percentage of data and create data
    according to that percentage.
"""
class ExpertGenerator(Generator):
    
    def __init__(self, data):
        super().__init__(data)

        self.optimum_data = []
        self.model = None

        self.percentages = []
        self.ndata = []

        self.arr_mini = []
        self.arr_maxi = []
        self.arr_mean = []

    def setModel(self, model):
        self.model = model

    def _findOptimumData(self, category_index = 1):
        # Get probabalities of model
        res = self.model.predict_proba(self.data)

        # Find the max value's index. But the ith column
        # It matters.
        # Old school for loop.
        for i in range(len(res)):
            for j in range(len(res[i])):
                pass
        



    def _findPercentages(self):
        raise NotImplementedError

    # @Override method
    def generate(self, datalen):
        
        self.optimum_data = self._findOptimumData()
        self.percentages = self._findPercentages()
