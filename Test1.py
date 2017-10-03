import unittest
from Add import *
from Subtract import *
from Mult import *
from Divide import *


class CalculatorTest(unittest.TestCase):
    
    def test_add(self):
        for i in range(-9999,9999,100):
            for j in range(-9999,9999,100):
                self.assertEqual(add(i,j), i+j)
        self.assertEqual(add(0,0),0)
    
    def test_sub(self):
        self.assertEqual(subtract(5,2), 3)

    def test_multiply(self):
        self.assertEqual(multiply(2,3), 6)

    def test_divide(self):
        self.assertEqual(divide(9,3), 3)
    
                  
   

if __name__ == '__main__':
    unittest.main()    


#https://jeffknupp.com/blog/2013/12/09/improve-your-python-understanding-unit-testing/
