from scipy.io import loadmat
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

raw_data = loadmat('Subject1_2D.mat')

left_forward1 = raw_data['LeftForward1']
left_forward2 = raw_data['LeftForward2']
left_forward3 = raw_data['LeftForward3']
left_forwardim = raw_data['LeftForwardImagined']

pl1 = pd.DataFrame(left_forward1)
pl2 = pd.DataFrame(left_forward2)
pl3 = pd.DataFrame(left_forward3)
plim = pd.DataFrame(left_forwardim)


complete_data = pd.concat([pl1, pl2, pl3, plim])

print("Complete Data Values")
print(complete_data.describe())

print("Left Forward-1 Values")
print(pl1.describe())
print("Left Forward-2 Values")
print(pl2.describe())
print("Left Forward-3 Values")
print(pl3.describe())
print("Left Forward-Im Values")
print(plim.describe())

all_min = [complete_data.describe()[i]['min'] for i in range(19)]
all_max = [complete_data.describe()[i]['max'] for i in range(19)]
all_mean = [complete_data.describe()[i]['mean'] for i in range(19)]
# print("All min : ",all_min)

# print("Unique Value: ",complete_data.describe()[0]['min'])
plt.plot(range(0,19), all_min)
plt.plot(range(0,19), all_mean)
plt.plot(range(0,19),all_max)

plt.scatter(range(0,19), all_min)
plt.scatter(range(0,19),all_mean)
plt.scatter(range(0,19), all_max)

# plt.legend()
plt.show()