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

    def getGraph(self, value):
        df = self.df
        if value == "gender":
            valueCounts = df["gender"].value_counts()
        elif value == "heart_disease":
            valueCounts = df["heart_disease"].value_counts()

        return valueCounts

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
        result = parameters.loc[parameters.age == age, "age"].count()

        print(result)
        return result
