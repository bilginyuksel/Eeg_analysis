import pandas as pd
from typo.gasic import BasicGenerator
from typo.gediu import MediumGenerator
from scipy.io import loadmat

import pickle


class SyntheticDataGenerator:

    # Maybe create engine on start.
    def __init__(self):
        pass

    def basic_generator_engine(self, data, datalen = 99):
        basic_engine = BasicGenerator(data)
        
        # Return dataframe or numpy
        # For scientific calculations numpy is better but 
        # you need to find out how to calculate things for numpy
        return pd.DataFrame(basic_engine.generate(datalen))

    def medium_generator_engine(self, data, datalen = 99):
        medium_engine = MediumGenerator(data)
        return pd.DataFrame(medium_engine.generate(datalen))

    def expert_generator_engine(self, data, datalen = 99):
        pass

    def advanced_generator_engine(self, data, datalen = 99):
        pass

   


model = pickle.load(open('C:/Users/bilgi/Documents/Yuksel Documents/BCI/BCI/Eeg_analysis/simulation/Random Forest Classifier.sav','rb'))
logreg = pickle.load(open('C:/Users/bilgi/Documents/Yuksel Documents/BCI/BCI/Eeg_analysis/simulation/Logistic Regression.sav','rb'))


raw_data = loadmat('C:/Users/bilgi/Documents/Yuksel Documents/BCI/BCI/Eeg_analysis/tests/Subject1_2D.mat')

lback_data = pd.concat([pd.DataFrame(raw_data['LeftBackward1']),
    pd.DataFrame(raw_data['LeftBackward2']),
    pd.DataFrame(raw_data['LeftBackward3']),
    pd.DataFrame(raw_data['LeftBackwardImagined'])])

synthetic = SyntheticDataGenerator()
result = synthetic.basic_generator_engine(lback_data)
result2 = synthetic.medium_generator_engine(lback_data, datalen=100)

result = pd.DataFrame(result)
result2 = pd.DataFrame(result2)
# print("Result2 : ",result2)
# print(result)
# print(result.loc[:1])
mod_res = model.predict(result.loc[:])
mod_res2 = model.predict(result2.loc[:])

probabilities = logreg.predict_proba(result2.loc[10:12])
for i in range(len(probabilities)):
    tmp = []
    max_index = 0
    for j in range(len(probabilities[i])):
        if probabilities[i][max_index] < probabilities[i][j]:
            max_index = j
        # tmp.append( probabilities[i][j] * 100 )
    print("Max Index : ",max_index)
    # print(tmp)
    
print(probabilities)
print(logreg.predict(result2.loc[10:12]))
# print()
# print()
# print(logreg.predict_log_proba(result2.loc[10:12]))

count = 0
count2 = 0

for i in mod_res: 
    if i == "LeftBackward": count+=1

for i in mod_res2:
    if i=="LeftBackward": count2+=1


print("Count of 99 : ",count)
print("Count of 100 : ",count2)