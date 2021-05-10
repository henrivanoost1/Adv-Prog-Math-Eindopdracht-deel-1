import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import json


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
            arr_value = []
            aantal_man = df[df["gender"] == "Male"].id.count()
            arr_value.append(str(aantal_man))
            aantal_vrouw = df[df["gender"] == "Female"].id.count()
            arr_value.append(str(aantal_vrouw))
            aantal_anders = df[df["gender"] == "Other"].id.count()
            arr_value.append(str(aantal_anders))
            array_to_json = json.dumps(arr_value)
            # arr_value[aantal_man, aantal_vrouw, aantal_anders]
        elif value == "heart_disease":
            valueCounts = df["heart_disease"].value_counts()

        return array_to_json

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
