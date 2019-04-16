# Function with single parameter
def square(x):
    """ This is a doc string!! Here is where you explain fxn"""
    new_value = x ** 2
    return new_value
    # Can choose to print to console or RETURN to assign value elsewhere
        # print(new_value)
    
square_three = square(3)

print(square_three)




# Function with multiple parameters
def raise_to_power(value1, value2):
    """Raise value1 to the power of value2"""
    value1_2 = value1 ** value2
    value2_1 = value2 ** value1
    
    new_tuple = (value1_2, value2_1)
    return(new_tuple)

result = raise_to_power(2,3)
print(result)



# Tuples
even_nums = (2, 4, 6)
print(even_nums[0]) # Respond to list indexing

# Tuples can be unpacked into independent variables
a, b, c = even_nums
print(a)
print(b)
print(c)




###### Functions final exercise ######
import pandas as pd

# Define count_entries()
def count_entries(df, col_name):
    """Return a dictionary with counts of 
    occurrences as value for each key."""

    # Initialize an empty dictionary: langs_count
    langs_count = {}
    
    # Extract column from DataFrame: col
    col = df[col_name]
    
    # Iterate over lang column in DataFrame
    for entry in col:

        # If the language is in langs_count, add 1
        if entry in langs_count.keys():
            langs_count[entry] += 1
        # Else add the language to langs_count, set the value to 1
        else:
            langs_count[entry] = 1

    # Return the langs_count dictionary
    return langs_count

tweets_df = pd.read_csv("tweets.csv")

# Call count_entries(): result
result = count_entries(tweets_df, 'lang')

# Print the result
print(result)