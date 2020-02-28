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

    def test_generated_left_backward_rf_score(self, data):
        return -1


    def test_generated_left_backward_lr_score(self, data):
        return -1


    def test_generated_left_backward_knn_score(self, data):
        return -1


    def test_generated_left_backward_dt_score(self, data):
        return -1


    # It runs all tests with generated data sent as a parameter.
    # When it runs all test it returns a tuple of scores.
    # Order of scores (Random Forest, Logistic Regression, KNN, Decision Tree)
    def runAll(self, generated_data):
        rf_score = self.test_generated_left_backward_dt_score(data)
        lr_score = self.test_generated_left_backward_lr_score(data)
        knn_score = self.test_generated_left_backward_knn_score(data)
        dt_score = self.test_generated_left_backward_dt_score(data)

        return (rf_score, lr_score, knn_score, dt_score)


generator = SyntheticDataGenerator()
data = generator.generate_left_backward_data(raw_data, datalen = 100)

left_arm_test = LeftArmBackwardTest()
rf_score = left_arm_test.test_generated_left_backward_rf_score(data)


