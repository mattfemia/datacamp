import pandas as pd

df = pd.read_csv("dob_job_application_filings_subset.csv")

##### Diagnosing data

# First and last 5 rows
df.head()
df.tail()

# Column names
df.columns

# Rows and column information
df.shape

# Additional info about data
print(df.info())




##### Exploratory data analysis

# df.describe allows us to look at numerical data in columns
print(df.describe)

# .value_counts allows us to look at categorical data

# Print the value counts for 'Borough'
print(df['Borough'].value_counts(dropna=False))

# Print the value_counts for 'State'
print(df["State"].value_counts(dropna=False))

# Print the value counts for 'Site Fill'
print(df["Site Fill"].value_counts(dropna=False))



###### Visual exploratory data analysis
import matplotlib.pyplot as plt

# Describe the column
df['Existing Zoning Sqft'].describe()

# Plot the histogram
df['Existing Zoning Sqft'].plot(kind='hist', rot=70, logx=True, logy=True)

# Display the histogram
plt.show()
