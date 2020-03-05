from scipy.io import loadmat
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

raw_data = loadmat('C:/Users/bilgi/Documents/Yuksel Documents/BCI/BCI/Eeg_analysis/tests/Subject1_2D.mat')

left_leg = raw_data['LeftLeg']
right_leg = raw_data['RightLeg']


pll = pd.DataFrame(left_leg)
prl = pd.DataFrame(right_leg)

print("Right Leg")
print(prl.describe())

print("Left Leg")
print(pll.describe())

all_min = [pll.describe()[i]['min'] for i in range(19)]
all_max = [pll.describe()[i]['max'] for i in range(19)]
all_mean = [pll.describe()[i]['mean'] for i in range(19)]
print("All min : ",all_min)

all_minr = [prl.describe()[i]['min'] for i in range(19)]
all_maxr= [prl.describe()[i]['max'] for i in range(19)]
all_meanr = [prl.describe()[i]['mean'] for i in range(19)]

# print("Unique Value: ",complete_data.describe()[0]['min'])
plt.plot(range(0,19), all_min)
plt.plot(range(0,19), all_mean)
plt.plot(range(0,19),all_max)

plt.plot(range(0,19), all_minr)
plt.plot(range(0,19), all_meanr)
plt.plot(range(0,19),all_maxr)


plt.scatter(range(0,19), all_min)
plt.scatter(range(0,19),all_mean)
plt.scatter(range(0,19), all_max)

plt.scatter(range(0,19), all_minr)
plt.scatter(range(0,19),all_meanr)
plt.scatter(range(0,19), all_maxr)

plt.legend()
plt.show()