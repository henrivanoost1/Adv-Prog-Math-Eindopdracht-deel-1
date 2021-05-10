import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv


class dataHandler():

    def __init__(self):
        self.df = self.getData()

    def getData(self):
        df = pd.read_csv("data\healthcare-dataset-stroke-data.csv")

        # print(test1)
        print(test2)

        # chart of chosen subject
        valueCounts = df["gender"].value_counts()
        valueCounts.plot.bar()
        plt.ylabel('Counts')
        plt.title("Gender")
        plt.show()
        return df

    def getStatistics(self):
        df = self.df
        # statistics of age
        statistics = df["age"].describe()
        return statistics

    def getParameters(self):
         # parameters
        df = self.df
        parameters = df.round(0)
        test2 = parameters.loc[parameters.age == 1, "age"].count()
        return test2
