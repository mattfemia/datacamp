##### Scope and user-defined functions


# Global vs Local Scope
def square(value):
    """Returns the square of a number"""
    new_val = value ** 2
    return new_val

print(square(3))

# print(new_val) 
    # Throws error because can't var isn't global scope


    
# Global vs Local Scope(2)
new_vals = 10

def squares(values):
    """Returns the square of a number"""
    new_vals = values ** 2
    return new_vals

print(squares(3)) # prints 9 because applying within fxn vars

print(new_vals) # prints 10 because we defined new_vals in global scope


# Global vs Local Scope(3)
new_valss = 10

def squaress(valuess):
    """Returns the square of a number"""
    global new_valss
    new_valss = new_valss ** 2
    return new_valss

print(squaress(3))

print(new_valss) # Responds to global new_valss iINSIDE fxn 
