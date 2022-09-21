import math
import unittest

def main():
    pass

##This function takes two number inputs, multiplies them, 
##and returns the result.
def multiplication(n1, n2):
    result = n1 * n2
    print('The result is: ', result)
   
##Adding feature for calculator
def adding(x,y):
    return(x+y)

##This function subtracts y from x :)
def subtract(x,y):
    return(x-y)
 
##This functions two numbers, x (the numerator) and y (the denominator),
##and returns the division of x by y.
def divide(x, y):
    return (x/y)

##This function takes in two numbers, x (the numerator) and y (the denominator),
##and returns the largest whole division of x by y, and the remainder
def divideWithRemainder(x, y):
    return math.floor(x/y), x%y



class Tests(unittest.TestCase):
    def testAdd(self):  #method that tests the program's functions 
        self.assertEqual(adding(4,2),6) #testing addition feature
        
    def testDivide(self):  #method that tests the program's functions 
        self.assertEqual(divide(7,2),3.5) #testing division feature
        
    def testDivideWithRemainder(self):  #method that tests the program's functions 
        self.assertEqual(divideWithRemainder(9,2),(4,1)) #testing division feature with remainder
    
    def testMultiplication(self): #method that tests the program's functions
        self.assertEqual(multiplication(4, 5), 20) #testing multiplication feature.
        
if __name__ == '__main__':
    unittest.main()

