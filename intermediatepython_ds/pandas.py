import pandas as pd

names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {"country": names, "drives_right": dr, "cars_per_cap": cpc}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars
print(cars)

# Import from csv file
    # x_file = pd.read_csv("x_file.csv", index_col=0)


##### Pandas series vs dataframe
    
# Print out country column as Pandas Series
print(cars["country"])

# Print out country column as Pandas DataFrame
print(cars[["country"]])

# Print out DataFrame with country and drives_right columns
print(cars[["country", "drives_right"]])


###### Indexing

# Print out first 3 observations
print(cars[0:3])
print("\n")

# Print out fourth, fifth and sixth observation
print(cars[3:6])
print("\n")

# iloc = integer-based |||| loc = label-based selections
print(cars.loc['RU'])
print(cars.iloc[4])
print("\n")

print(cars.loc[['RU']])
print(cars.iloc[[4]])
print("\n")

print(cars.loc[['RU', 'AUS']])
print(cars.iloc[[4, 1]])
print("\n")


# Print out drives_right column as Series
print(cars.loc[:,"drives_right"])

# Print out drives_right column as DataFrame
print(cars.loc[:,["drives_right"]])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:, ["cars_per_cap", "drives_right"]])