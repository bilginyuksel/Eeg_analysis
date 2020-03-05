import matplotlib.pyplot as plt
from scipy.io import loadmat
import pandas as pd
import numpy as np
import sys
sys.path.append(".")
from generator.synthetic import SyntheticDataGenerator

# plt.ion() ## Note this correction
# fig=plt.figure()
# plt.axis([0,1000,0,1])
plt.title("Basic Synthetic Data Generation")

"""
load data and set the generator.
"""
raw_data = loadmat('C:/Users/bilgi/Documents/Yuksel Documents/BCI/BCI/Eeg_analysis/tests/Subject1_2D.mat')
data = pd.DataFrame(raw_data['LeftBackward1'])
generator = SyntheticDataGenerator(data)
generator.configGenerator("Basic")


for _ in range(100):
    plt.plot(generator.generateSyntheticData(1));
    # plt.title("Synthetic Data Generator")
    # plt.show()
    plt.pause(0.0001) #Note this correction
else:
    plt.show()