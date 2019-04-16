###### Importing and reading text files

practice = "C:/Users/matth/Developer/datacamp/importdata1/practice.txt"

# Reading into a file
file = open(practice, mode="r") 

# Assign text in file to variable
text = file.read()

# Close the file
file.close()

# Print to console
print(text)

# OR

# To autoclose after read
with open("practice.txt") as file:
    print(file.read())




##### Importing and reading CSV/txt

print("Flat files have delimiters to separate values")

# Importing flat files using NumPy
import numpy as np

# Import file
filename = "titanic.csv"

# Use np.loadtxt method. Add skiprows to skip over header
data = np.loadtxt(filename, delimiter=",", skiprows=1, usecols=[0, 1, 2])
print(data)

# loadtxt as strings instead of float using dtype=str
data = np.loadtxt(filename, delimiter=",", skiprows=1, dtype=str)
print(data)

## For mixed datasets with mixed types use np.genfromtxt
data = np.genfromtxt(filename, delimiter=",", names=True, dtype=None)
        # names = True -- there's a header
        # dtype = None -- mixed data types
print(data)

## Alternative to np.genfromtxt
d = np.recfromcsv(filename)
        # Defauls: names=True, dtype=None, delimiter=","
print(d)




##### Importing flat files using pandas
import pandas as pd

filename = "titanic.csv"

data = pd.read_csv(filename)

print(data.head())

data_array = data.values

print(data_array)

# Read the first 5 rows of the file into a DataFrame: data
data = pd.read_csv(filename, nrows=5, header=None)

# Build a numpy array from the DataFrame: data_array
data_array = np.array(data)

# Print the datatype of data_array to the shell
print(type(data_array))

# If file has missing values(Na or NaN or "Nothing") or comment characters("#")
    # data = pd.read_csv(filename, sep="\t", comment="#", na_values="Nothing")