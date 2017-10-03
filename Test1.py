import unittest
from Add import add
from Subtract import subtract 
from Mult import multiply
from Divide import divide


class CalculatorTest(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(0,9), 9)
        print 
    
    def test_sub(self):
        self.assertEqual(subtract(5,2), 3)

    def test_multiply(self):
        self.assertEqual(multiply(2,3), 6)

    def test_divide(self):
        self.assertEqual(divide(9,3), 3)
    
                  
   

if __name__ == '__main__':
    unittest.main()    


#https://jeffknupp.com/blog/2013/12/09/improve-your-python-understanding-unit-testing/
