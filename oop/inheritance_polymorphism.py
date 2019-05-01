#1 Inheritance ex.) Animal inheritance

# Create a class Animal
class Animal:
	def __init__(self, name):
		self.name = name

# Create a class Mammal, which inherits from Animal
class Mammal(Animal):
	def __init__(self, name, animal_type):
		self.animal_type = animal_type

# Create a class Reptile, which also inherits from Animal
class Reptile(Animal):
	def __init__(self, name, animal_type):
		self.animal_type = animal_type

# Instantiate a mammal with name 'Daisy' and animal_type 'dog': daisy
daisy = Mammal('Daisy', 'dog')

# Instantiate a reptile with name 'Stella' and animal_type 'alligator': stella
stella = Reptile('Stella', 'alligator')

# Print both objects
print(daisy)
print(stella)



#2 Inheritance ex.) Vertebrate inheritance


# Create a class Vertebrate
class Vertebrate:
    spinal_cord = True
    def __init__(self, name):
        self.name = name

# Create a class Mammal, which inherits from Vertebrate
class Mammal(Vertebrate):
    def __init__(self, name, animal_type):
        self.animal_type = animal_type
        self.temperature_regulation = True

# Create a class Reptile, which also inherits from Vertebrate
class Reptile(Vertebrate):
    def __init__(self, name, animal_type):
        self.animal_type = animal_type
        self.temperature_regulation = False

# Instantiate a mammal with name 'Daisy' and animal_type 'dog': daisy
daisy = Mammal('Daisy', 'dog')

# Instantiate a reptile with name 'Stella' and animal_type 'alligator': stella
stella = Reptile('Stella', 'alligator')

# Print stella's attributes spinal_cord and temperature_regulation
print("Stella Spinal cord: " + str(stella.spinal_cord))
print("Stella temperature regularization: " + str(stella.temperature_regulation))

# Print daisy's attributes spinal_cord and temperature_regulation
print("Daisy Spinal cord: " + str(daisy.spinal_cord))
print("Daisy temperature regularization: " + str(daisy.temperature_regulation))



#3 Class inheritance


# Load numpy as np and pandas as pd
import numpy as np
import pandas as pd

# Create class: DataShell
class DataShell:
    def __init__(self, inputFile):
        self.file = inputFile

# Create class CsvDataShell, which inherits from DataShell
class CsvDataShell(DataShell):
    # Initialization method with arguments self, inputFile
    def __init__(self, inputFile):
        # Instance variable data
        self.data = pd.read_csv(inputFile)

# Instantiate CsvDataShell as us_data_shell, passing us_life_expectancy as argument
us_data_shell = CsvDataShell(us_life_expectancy)

# Print us_data_shell.data
print(us_data_shell.data)



#4 Composed classes -- inherits functionality from other classes

# Define abstract class DataShell
class DataShell:
    # Class variable family
    family = 'DataShell'
    # Initialization method with arguments, and instance variables
    def __init__(self, name, filepath): 
        self.name = name
        self.filepath = filepath

# Define class CsvDataShell      
class CsvDataShell(DataShell):
    # Initialization method with arguments self, name, filepath
    def __init__(self, name, filepath):
        # Instance variable data
        self.data = pd.read_csv(filepath)
        # Instance variable stats
        self.stats = self.data.describe()

# Instantiate CsvDataShell as us_data_shell
us_data_shell = CsvDataShell("US", us_life_expectancy)

# Print us_data_shell.stats
print(us_data_shell.stats)