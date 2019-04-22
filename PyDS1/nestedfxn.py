# Nested Function: basic

def mod2plus5(x1, x2, x3):
    """Returns the remainder plus 5 of three values"""
    
    def inner(x):
        """Returns the remainder plus 5 of a value"""
        return x % 2 + 5
    
    return (inner(x1), inner(x2), inner(x3))
print(mod2plus5(1, 2, 3))



# Nested Function: returning function as value
def raise_val(n):
    """Return the inner function"""
    
    def inner(x):
        """Raise x to the power of n"""
        raised = x ** n
        return raised
    
    return inner

square = raise_val(2)
cube = raise_val(3)

print(square(2), cube(4))


