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
        # self.plotter.title(self.title)
        pass

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
        self.generator.configGenerator('Medium')
        basic_generator = SyntheticDataGenerator(self.data)
        basic_generator.configGenerator('Basic')
        medium_generator = SyntheticDataGenerator(self.data)
        medium_generator.configGenerator('Medium')
        # self.generator.configGenerator('Medium')
        # Plot all with subplots to see same data for all
        # kind of generators also for real genersator too
        fig, ax = self.plotter.subplots(2,2, figsize = (12,7))
        count = 0
        real_data = self.data
        for _ in range(40):
            ax[0][0].plot(basic_generator.generateSyntheticData(1))
            ax[0][0].set_title("Basic Generator")
            ax[1][0].plot(medium_generator.generateSyntheticData(1))
            ax[1][0].set_title("Medium Generator")
            ax[0][1].plot(self.generator.generateSyntheticData(1))
            ax[0][1].set_title("Expert Generator")
            count+=1
            ax[1][1].plot(real_data.loc[count:count+1])            
            ax[1][1].set_title("Real Data")
            self.plotter.pause(0.0001)
        else:
            ax[1][1].plot(self.data.loc[0:40])
            self.plotter.show()



plots = SyntheticDataGenerationPlots(pd.DataFrame(loadmat('C:/Users/bilgi/Documents/Yuksel Documents/BCI/BCI/Eeg_analysis/tests/Subject1_2D.mat')['LeftBackward1']),"Synthetic Data")
plots.configPlot()
plots.plotAll()