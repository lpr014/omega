import unittest
from Add import add
from Subtract import subtract 
from Subtract import subtract
from Mult import multiply
from Divide import divide


class CalculatorTest(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(0,9), 9)
    
    def test_sub(self):
        self.assertEqual(subtract(5,2), 3)

    def test_multiply(self):
        self.assertEqual(multiply(2,3), 6)

    def test_divide(self):
        self.assertEqual(divide(9,3), 3)
    
                  
   

if __name__ == '__main__':
    unittest.main()    


<<<<<<< HEAD

#https://jeffknupp.com/blog/2013/12/09/improve-your-python-understanding-unit-testing/
=======
#https://jeffknupp.com/blog/2013/12/09/improve-your-python-understanding-unit-testing/
>>>>>>> c1f878bc77ed5232f06f244a8ebd03d6b1f4f642
