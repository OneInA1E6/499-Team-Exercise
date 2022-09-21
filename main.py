import math
import unittest

def main():
    pass

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
    def test(self):  #method that tests the function 
        self.assertEqual(adding(4,2),6) #testing addition feature
        
if __name__ == '__main__':
    unittest.main()

