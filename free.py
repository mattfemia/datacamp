import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = pd.read_csv("importdata1/titanic.csv")


data_array = np.array(file)
print(data_array)

np.describe(data_array)