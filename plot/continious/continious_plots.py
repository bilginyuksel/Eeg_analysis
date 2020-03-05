import matplotlib.pyplot as plt
import pandas as pd
from scipy.io import loadmat
import sys
sys.path.append(".")
from generator.synthetic import SyntheticDataGenerator



class SyntheticDataGenerationPlots:

    def __init__(self, data, title):
        # Load data which is going to generated
        self.data = data
        self.title = title
        self.generator = SyntheticDataGenerator(self.data)
        self.plotter = plt

    def configPlot(self):
        self.plotter.title(self.title)

    def plotReal(self):
        pass

    def plotBasic(self):
        self.generator.configGenerator('Basic')

        # Plot data here with this generated data
        for _ in range(100):
            self.plotter.plot(self.generator.generateSyntheticData(1))
            self.plotter.pause(0.0001)
        else:
            self.plotter.show()

    def plotMedium(self):
        self.generator.configGenerator('Medium')

        # Plot data here with this generated data
        for _ in range(100):
            self.plotter.plot(self.generator.generateSyntheticData(1))
            self.plotter.pause(0.0001)
        else:
            self.plotter.show()

    def plotExpert(self):
        generator = SyntheticDataGenerator(self.data)
        generator.configGenerator('Expert', None, None)
        
        # Plot data here with this generated data
        generator.generateSyntheticData(1)

    def plotAll(self):
        # Plot all with subplots to see same data for all
        # kind of generators also for real genersator too
        pass



plots = SyntheticDataGenerationPlots(pd.DataFrame(loadmat('C:/Users/bilgi/Documents/Yuksel Documents/BCI/BCI/Eeg_analysis/tests/Subject1_2D.mat')['LeftBackward1']),"Synthetic Data")
plots.configPlot()
plots.plotBasic()