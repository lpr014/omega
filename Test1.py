## from _____ import the class ##


from unittest import TestCase

class CalculatorTest(unittest.TestCase):
    
    def setUp(self):

        self.calc = src.calculator.Calculator()
    
    def test_add(self):
        self.assertEqual(self.calc.add(0,9), 9)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2,3), 6)

    def test_divide(self):
        self.assertEqual(self.calc.divide(9,3), 3)
              


if __name__ == '__main__':
    main()    
