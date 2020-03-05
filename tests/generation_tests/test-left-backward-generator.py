import pickle
import pandas as pd
from scipy.io import loadmat
from basic_generator import SyntheticDataGenerator

# Load pretrained models.
rf_model = pickle.load(open('Random Forest Classifier.sav','rb'))
lr_model = pickle.load(open('Logistic Regression.sav','rb'))
knn_model = pickle.load(open('KNeighbors Classifier.sav','rb'))
dt_model = pickle.load(open('Decision Tree Classifier.sav','rb'))

# Load raw data.
raw_data = loadmat('Subject1_2D.mat')
"""
Create much detailed test cases.
Find its neighbors, or find the percentage the correctnes.
"""

class LeftArmBackwardTest:

    def __init__(self, data, models):
        self.data = data
        self.generator = SyntheticDataGenerator()

        # Models is a dictionary which contains machine learning models
        # self.models['rf']
        # self.models['lr']
        # self.models['knn']
        # self.models['dt]
        self.models = models
        

    def test_generated_left_backward_rf_score(self):

        
        return -1


    def test_generated_left_backward_lr_score(self):
        return -1


    def test_generated_left_backward_knn_score(self):
        return -1


    def test_generated_left_backward_dt_score(self):
        return -1


    # It runs all tests with generated data sent as a parameter.
    # When it runs all test it returns a tuple of scores.
    # Order of scores (Random Forest, Logistic Regression, KNN, Decision Tree)
    def runAll(self, generated_data):

        return (self.test_generated_left_backward_dt_score(),
                self.test_generated_left_backward_lr_score(),
                self.test_generated_left_backward_knn_score(),
                self.test_generated_left_backward_dt_score())


# Prepare data and models
models = {
    'rf':rf_model,
    'lr':lr_model,
    'dt':dt_model,
    'knn':knn_model
}
data = pd.DataFrame(raw_data)

left_arm_test = LeftArmBackwardTest(data, models)
rf_score = left_arm_test.test_generated_left_backward_rf_score()


