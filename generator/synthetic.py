import pandas as pd
from scipy.io import loadmat
import pickle
import sys
sys.path.append(".")
from .typo.gasic import BasicGenerator
from .typo.gediu import MediumGenerator
from .typo.gexp import ExpertGenerator



class SyntheticDataGenerator:

    def __init__(self, data):
        
        self.data = data
        self.generator = None
        self.synthetic_data = ()

    def _basic_generator_engine_configuration(self):
        self.generator = BasicGenerator(self.data)
        self.generator.configure()

    def _medium_generator_engine_configuration(self):
        self.generator = MediumGenerator(self.data)
        self.generator.configure()

    def _expert_generator_engine_configuration(self,desired_index, model):
        self.generator = ExpertGenerator(self.data, desired_index)
        self.generator.setModel(model)
        self.generator.configure()

    def configGenerator(self, genType, desired_index = None, model = None):
        if genType == "Basic":
            self._basic_generator_engine_configuration()
        elif genType == 'Medium':
            self._medium_generator_engine_configuration()
        elif genType == 'Expert':
            self._expert_generator_engine_configuration(desired_index, model)

    # You may choose to return array or numpy array instead of dataframe
    def generateSyntheticData(self, datalen):
        return pd.DataFrame(self.generator.generate(datalen))



   

model = pickle.load(open('C:/Users/bilgi/Documents/Yuksel Documents/BCI/BCI/Eeg_analysis/simulation/Random Forest Classifier.sav','rb'))
logreg = pickle.load(open('C:/Users/bilgi/Documents/Yuksel Documents/BCI/BCI/Eeg_analysis/simulation/Logistic Regression.sav','rb'))


raw_data = loadmat('C:/Users/bilgi/Documents/Yuksel Documents/BCI/BCI/Eeg_analysis/tests/Subject1_2D.mat')

lback_data = pd.concat([pd.DataFrame(raw_data['LeftBackward1']),
    pd.DataFrame(raw_data['LeftBackward2']),
    pd.DataFrame(raw_data['LeftBackward3']),
    pd.DataFrame(raw_data['LeftBackwardImagined'])])

synthetic = SyntheticDataGenerator(lback_data)
synthetic.configGenerator("Basic")
result = synthetic.generateSyntheticData(400)

synthetic1 = SyntheticDataGenerator(lback_data)
synthetic1.configGenerator("Medium")
result2 = synthetic1.generateSyntheticData(1000)

result = pd.DataFrame(result)
result2 = pd.DataFrame(result2)
# print("Result2 : ",result2)
# print(result)
# print(result.loc[:1])
mod_res = model.predict(result.loc[:])
mod_res2 = model.predict(result2.loc[:])



count = 0
# count2 = 0
lf = 0
lb = 0
rf = 0
rb = 0
rl = 0
ll = 0

for i in mod_res: 
    if i == "LeftBackward": count+=1

for i in mod_res2:
    if i=="LeftBackward": lb+=1
    elif i == 'LeftForward': lf+=1
    elif i == 'RightBackward': rb+=1
    elif i == 'RightForward': rf+=1
    elif i == 'LeftLeg': ll+=1
    else: rl += 1


def giveMeMyData():
    return result2, mod_res2

# print("Count of 99 : ",count)
print("Left Backward : ",lb)
print("Left Forward : ",lf)
print("Right Forward : ",rf)
print("Right Backward : ",rb)
print("Left Leg : ",ll)
print("Right Leg : ",rl)

# synthetic.expert_generator_engine( logreg)
# print(mod_res2)
