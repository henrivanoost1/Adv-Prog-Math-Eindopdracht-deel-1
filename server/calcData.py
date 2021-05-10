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
        # getParameters(1)

        # chart of chosen subject
        # valueCounts = df["gender"].value_counts()
        # valueCounts.plot.bar()
        # plt.ylabel('Counts')
        # plt.title("Gender")
        # plt.show()
        return df

    def getStatistics(self):
        df = self.df
        # statistics of age
        statistics = df["age"].describe()
        return statistics

    def getParameters(self, age1):
         # parameters
        # df = pd.read_csv("data\healthcare-dataset-stroke-data.csv")
        df = self.df
        parameters = df.round(0)
        age = int(age1)
        result = parameters.loc[parameters.age == age1, "age"].count()
        result
        print(result)
        return result
