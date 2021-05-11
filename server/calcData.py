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
            aantal_man = df[df["gender"] == "Male"].where(
                df["stroke"] == 1).id.count()
            arr_value.append(str(aantal_man))
            aantal_vrouw = df[df["gender"] == "Female"].where(
                df["stroke"] == 1).id.count()
            arr_value.append(str(aantal_vrouw))
            aantal_anders = df[df["gender"] == "Other"].where(
                df["stroke"] == 1).id.count()
            arr_value.append(str(aantal_anders))
            array_to_json = json.dumps(arr_value)
            # arr_value[aantal_man, aantal_vrouw, aantal_anders]
        elif value == "heart_disease":
            arr_value = []
            aantal_yes = df[df["heart_disease"] == 1].where(
                df["stroke"] == 1).id.count()
            arr_value.append(str(aantal_yes))
            aantal_no = df[df["heart_disease"] == 0].where(
                df["stroke"] == 1).id.count()
            arr_value.append(str(aantal_no))
            array_to_json = json.dumps(arr_value)

        return array_to_json

    def getStatistics(self):
        df = self.df
        # statistics of age
        statistics = df["age"].describe()
        json1 = "{"+f'"Type": {statistics.index.values.tolist()}, "Value": {statistics.values.tolist()}'+"}"
        json1 = json1.replace("'", '"')
        return json1
        # json_temp = json.loads(json1)

    def getParameters(self, age1):
         # parameters
        # df = pd.read_csv("data\healthcare-dataset-stroke-data.csv")
        df = self.df

        age = int(age1)
        result = df[df["age"] == age].where(df["stroke"] == 1).id.count()

        print(result)
        return result
