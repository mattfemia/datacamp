
def power(val, pow=1):
    """ Raise value to power of pow"""
    return val ** pow

test = power(2, 3)
print(test)

test2 = power(5)
print(test2)

def add_all(*args):
    """ Sum of all values in args together """
    
    sum_all = 0
    
    for num in args:
        sum_all += num
        
    return sum_all

prac = add_all(1,2,3,4,5,6,7,278)
print(prac)


def print_all(**kwargs):
    for key, value in kwargs.items():
        print(key + ": " + value)
    
prac2 = print_all(job="investigator", salary="200k", status="current")
print(prac2)
