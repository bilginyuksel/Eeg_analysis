import numpy as np

class Generator:

    def __init__(self, data):
        self.data = data
        self.features = data.columns

    def generate(self, datalen):
        raise NotImplementedError

def dmini(data):
    return np.array(data.min())

def dmaxi(data):
    return np.array(data.max())

def dmean(data):
    return np.array(data.mean())