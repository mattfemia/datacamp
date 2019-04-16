import numpy as np
import pandas as pd

file = "titanic.csv"

data = pd.read_csv(file, sep=",", comment="#", na_values="Nothing")

                   
data_array = np.array(data)
gender = data_array[:, 3]

counterm = 0
counterf = 0


for x in gender:
    if x == "male":
        counterm = counterm + 1
    elif x == "female":
        counterf = counterf + 1
    else:
        print("error")

print(counterm)
print(counterf)