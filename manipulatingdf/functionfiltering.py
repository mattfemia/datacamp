import pandas as pd

#1 Using apply() to filter with fxn

# Write a function to convert degrees Fahrenheit to degrees Celsius: to_celsius
def to_celsius(F):
    return 5/9*(F - 32)

file = "pittsburgh2013.csv"
weather = pd.read_csv(file)

# Apply the function over 'Mean TemperatureF' and 'Mean Dew PointF': df_celsius
df_celsius = weather[['Mean TemperatureF', 'Mean Dew PointF']].apply(to_celsius)

# Reassign the columns df_celsius
df_celsius.columns = ['Mean TemperatureC', 'Mean Dew PointC']

# Print the output of df_celsius.head()
print(df_celsius.head())






#2 Using map() to apply a fxn to data

file = "pennsylvania2012_turnout.csv"
election = pd.read_csv(file)

# Create the dictionary: red_vs_blue
red_vs_blue = {'Obama':'blue', 'Romney': 'red'}

# Use the dictionary to map the 'winner' column to the new column: election['color']
election['color'] = election.loc[:, 'winner'].map(red_vs_blue)

# Print the output of election.head()
print(election.head())





#3 Using vectorized fxns --- these are preferred for code efficiency

# Import zscore from scipy.stats
from scipy.stats import zscore

# Call zscore with election['turnout'] as input: turnout_zscore
turnout_zscore = zscore(election['turnout'])

# Print the type of turnout_zscore
print(type(turnout_zscore))

# Assign turnout_zscore to a new column: election['turnout_zscore']
election['turnout_zscore'] = turnout_zscore

# Print the output of election.head()
print(election.head())