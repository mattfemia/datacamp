class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def subtract(self):
        print(self.num1 - self.num2)
    
    def add(self):
        return(self.num1 + self.num2)
    

threetwo = Calculator(3,2)

threetwo.subtract()

sum23 = threetwo.add()

print(sum23)

    