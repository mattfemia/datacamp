



def sumall(*args):
    sum = 0

    for arg in args:
        sum += arg
    
    return sum

fred = sumall(1, 2, 3, 4)

print(fred)


def sentenceBuilder(*kwargs):
    phrase = ""

    for word in kwargs:
        phrase += word + " "

    return phrase

newSentence = sentenceBuilder("doug", "is", "cool")

print(newSentence)

def innerOuter(x1, x2, x3):

    def inner(x):
        return x % 2 + 5
    
    return (inner(x1), inner(x2), inner(x3))

new = innerOuter(1, 2, 3)

print(new)

# lambda functions

newb = lambda x,y: x ** y

print(newb(2,3))


sentenceUpper = lambda word: word.upper()

success = sentenceUpper("fred")
print(success)


# map function

numbers = [1, 2, 3, 4, 5]
square_all = map(lambda nums: nums ** 2, numbers)
print(square_all)

square_all = list(square_all)
print(square_all)
