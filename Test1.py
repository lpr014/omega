class CalculatorTest(unittest.TestCase):
    
    def setUp(self):

        self.calc = src.calculator.Calculator()
    
    def test_add(self):
        self.assertEqual(self.calc.add(0,9), 9)
        pass

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2,3), 6)
        pass  
          