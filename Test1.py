## from _____ import the class ##


import unittest
from Mult import multiply

class CalculatorTest(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(2,3), 6)
    ''' 
        def setUp(self):
            self.calc = src.calculator.Calculator()
        
        def test_add(self):
            self.assertEqual(self.calc.add(0,9), 9)
    '''
    
    '''
        def test_divide(self):
            self.assertEqual(self.calc.divide(9,3), 3)
                  
    '''

if __name__ == '__main__':
    unittest.main()    
