import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
data = pd.read_csv("data\healthcare-dataset-stroke-data.csv")

# statistics of age
statistics = data["age"].describe()
print(statistics)

# parameters
parameters = data.round(0)
test2 = parameters.loc[parameters.age == 1, "age"].count()

# print(test1)
print(test2)


# chart of chosen subject
valueCounts = data["gender"].value_counts()
valueCounts.plot.bar()
plt.ylabel('Counts')
plt.title("Gender")
plt.show()
