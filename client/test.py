import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
data = pd.read_csv("client\healthcare-dataset-stroke-data.csv")

# statistics of age
statistics = data["age"].describe()
print(statistics)

# parameters
# age = data["age"].round(0)
# print(age)
parameters = data.round(0)
print(parameters)
test1 = data.loc[data.age == 1, "age"].count()
test2 = parameters.loc[parameters.age == 1, "age"].count()

print(test1)
print(test2)


# chart of chosen subject
valueCounts = data["gender"].value_counts()
valueCounts.plot.bar()
plt.ylabel('Counts')
plt.title("Gender")
plt.show()
