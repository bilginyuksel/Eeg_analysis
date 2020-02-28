from scipy.io import loadmat
import pandas as pd
import numpy as np

raw_data = loadmat('Subject1_2D.mat')

left_back1 = raw_data['LeftBackward1']
left_back2 = raw_data['LeftBackward2']
left_back3 = raw_data['LeftBackward3']
left_backim = raw_data['LeftBackwardImagined']

pl1 = pd.DataFrame(left_back1)
pl2 = pd.DataFrame(left_back2)
pl3 = pd.DataFrame(left_back3)
plim = pd.DataFrame(left_backim)


complete_data = pd.concat([pl1, pl2, pl3, plim])

print("Complete Data Values")
print(complete_data.describe())

print("Left Backward-1 Values")
print(pl1.describe())
print("Left Backward-2 Values")
print(pl2.describe())
print("Left Backward-3 Values")
print(pl3.describe())
print("Left Backward-Im Values")
print(plim.describe())