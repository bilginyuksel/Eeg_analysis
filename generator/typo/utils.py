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

def percentages2B(lowbound, curbound, upbound):
    """
    IT finds the distance percentage between current bound and lower bound
    according to data on the current bound. 
    """
    
    perc = []

    for lbound, cbound, ubound in zip(lowbound, curbound, upbound):
        dist_lbound = abs(cbound - lbound)
        dist_ubound = abs(cbound - ubound)

        dist_minimum = min(dist_lbound, dist_ubound)

        tmp_perc = (dist_minimum / cbound * 100)
        perc.append(tmp_perc)

    return perc


