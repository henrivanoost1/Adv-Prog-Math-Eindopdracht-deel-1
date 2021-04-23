import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
data = pd.read_csv("client\healthcare-dataset-stroke-data.csv")

# statistics of age
statistics = data["age"].describe()
print(statistics)

# chart of chosen subject
valueCounts = data["gender"].value_counts()
valueCounts.plot.bar()
plt.ylabel('Counts')
plt.title("Gender")
plt.show()

# parameters
