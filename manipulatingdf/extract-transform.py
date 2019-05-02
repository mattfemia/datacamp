
# =============================================================================
# Preparing file to be used (not in datacamp tutorial)
# =============================================================================
import pandas as pd

file = "pennsylvania2012_turnout.csv"

data = pd.read_csv(file)

df = pd.DataFrame(data) # or set ,index_col="count"

# Remove index
df.set_index("county", inplace=True)

# Use only the first 7 columns
df = df.iloc[:, :6]

# =============================================================================
# Tutorials
# =============================================================================

#1
# Your job is to select 'Bedford' county and the 'winner' column
print(df.loc['Bedford', 'winner'])



#2
# Indexing and Column Rearrangement

# Read in filename and set the index: election
election = pd.read_csv(file, index_col='county')

# Create a separate dataframe with the columns ['winner', 'total', 'voters']: results
results = pd.DataFrame(election[['winner', 'total', 'voters']])

# Print the output of results.head()
print(results.head())




#3 

# Slice the row labels 'Perry' to 'Potter': p_counties
p_counties = election.loc["Perry":"Potter"]

# Print the p_counties DataFrame
print(p_counties)

# Slice the row labels 'Potter' to 'Perry' in reverse order: p_counties_rev
p_counties_rev = election.loc["Potter":"Perry":-1]

# Print the p_counties_rev DataFrame
print(p_counties_rev)




#4 

# Slice the columns from the starting column to 'Obama': left_columns
left_columns = election.iloc[:, 0:3]

# Print the output of left_columns.head()
print(left_columns.head())

# Slice the columns from 'Obama' to 'winner': middle_columns
middle_columns = election.iloc[:, 2:5]

# Print the output of middle_columns.head()
print(middle_columns.head())

# Slice the columns from 'Romney' to the end: 'right_columns'
right_columns = election.iloc[:, 3:]

# Print the output of right_columns.head()
print(right_columns.head())





#5 Subselecting dataframes with lists

# Create the list of row labels: rows
rows = ['Philadelphia', 'Centre', 'Fulton']

# Create the list of column labels: cols
cols = ['winner', 'Obama', 'Romney']

# Create the new DataFrame: three_counties
three_counties = pd.DataFrame(election.loc[rows, cols])

# Print the three_counties DataFrame
print(three_counties)




#6 Filtering data with Boolean expression 

# Create the boolean array: high_turnout
high_turnout = election.loc[:, 'turnout'] > 70

# Filter the election DataFrame with the high_turnout array: high_turnout_df
high_turnout_df = election.loc[high_turnout]

# Print the high_turnout_results DataFrame
print(high_turnout_df)




#7 Filtering columns using other columns

# Import numpy
import numpy as np

# Create the boolean array: too_close
too_close = election['margin'] < 1

# Assign np.nan to the 'winner' column where the results were too close to call
election.loc[too_close, 'winner'] = np.nan

# Print the output of election.info()
print(election.info())




#8 Filtering using NaNs

file = "titanic.csv"
titanic = pd.read_csv(file)

# Select the 'age' and 'cabin' columns: df
df = titanic.loc[:, ['age','cabin']]

# Print the shape of df
print(df.shape)

# Drop rows in df with how='any' and print the shape
print(df.dropna(how='any').shape)

# Drop rows in df with how='all' and print the shape
print(df.dropna(how='all').shape)

# Drop columns in titanic with less than 1000 non-missing values
print(titanic.dropna(thresh=1000, axis='columns').info())





