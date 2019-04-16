##### Default Arguments

def power(number, pow=1):
    """raise number to the power of pow"""
    new_value = number ** pow
    return new_value

print(power(9,2)) # uses new value to perform fxn

print(power(9)) # uses default value to perform fxn



##### Flexible Numerical Arguments: *args

def add_all(*args):
    """Sum of all values in *args together"""
    
    #Initialize sum
    sum_all = 0
    
    for num in args:
        sum_all += num
    
    return sum_all

first = add_all(1, 2, 3, 4, 5)
print(first)




##### Flexible Keyword Arguments: **kwargs

def print_all(**kwargs):
    """Print out key-value pairs in **kwargs"""
    
    #Print out the key-value pairs
    for key, value in kwargs.items():
        print(key + ": " + value)

second = print_all(name="dumbledore", job="headmaster")
print(second)
        