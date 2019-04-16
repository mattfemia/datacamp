
# Select column of interest --> comparison on column --> use result to select data
    # If comparing multiple selections: np.logical_and() np.logical_or()


# For loop that displays index
fam = [1.73, 1.68, 1.71, 1.89]
for index, height in enumerate(fam) :
    print("index " + str(index) + ": " + str(height))


# Loop over list of lists

house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
for x in house:
    print("the " + x[0] + "is " + str(x[1])+ " sqm")


# Loop over dictionary
    # for key, val in my_dict.items
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
for key, value in europe.items() :
    print("the capital of " + key + " is " + str(value))


# Loop over numpy array
    # for val in np.nditer(my_array)
    
# Loop over numpy dataframe
    # for lab, row in brics.iterrows() :
    

# Adding column of data for each row of dataframe
    # Apply method: 
        # cars["COUNTRY"] = cars["country"].apply(str.upper)
    
    # For loop method:
        # for lab, row in cars.iterrows():
            # cars.loc[lab, "COUNTRY"] = row["country"].upper()