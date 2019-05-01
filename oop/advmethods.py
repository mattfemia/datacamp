# 1  Advanced return statement

# Load numpy as np and pandas as pd
import numpy as np
import pandas as pd

# Create class: DataShell
class DataShell:
  
    # Initialize class with self and inputFile
    def __init__(self, inputFile):
        self.file = inputFile
        
    # Define generate_csv method, with self argument
    def generate_csv(self):
        self.data_as_csv = pd.read_csv(self.file)
        return self.data_as_csv

# Instantiate DataShell with us_life_expectancy as input argument
data_shell = DataShell("us_life_expectancy.csv")

# Call data_shell's generate_csv method, assign it to df
df = data_shell.generate_csv()

# Print df
print(df)


#2 Data as attributes 

# Create class: DataShell
class DataShell:
  
    # Define initialization method
    def __init__(self, filepath):
        # Set filepath as instance variable  
        self.filepath = filepath
        # Set data_as_csv as instance variable
        self.data_as_csv = pd.read_csv(filepath)

# Instantiate DataShell as us_data_shell
us_data_shell = DataShell("us_life_expectancy.csv")

# Print your object's data_as_csv attribute
print(us_data_shell.data_as_csv)




#3 Renaming columns in data


# Create class DataShell
class DataShell:
  
    # Define initialization method
    def __init__(self, filepath):
        self.filepath = filepath
        self.data_as_csv = pd.read_csv(filepath)
    
    # Define method rename_column, with arguments self, column_name, and new_column_name
    def rename_column(self, column_name, new_column_name):
        self.data_as_csv.columns = self.data_as_csv.columns.str.replace(column_name, new_column_name)

# Instantiate DataShell as us_data_shell with argument us_life_expectancy
us_data_shell = DataShell("us_life_expectancy.csv")

# Print the datatype of your object's data_as_csv attribute
print(us_data_shell.data_as_csv.dtypes)

# Rename your objects column 'code' to 'country_code'
us_data_shell.rename_column('code', 'country_code')

# Again, print the datatype of your object's data_as_csv attribute
print(us_data_shell.data_as_csv.dtypes)