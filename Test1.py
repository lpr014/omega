#Last edit by Lorantz 10/5/17 @ 1749

import unittest
import math
from Add import *
from Subtract import *
from Mult import *
from Divide import *
from SquareRoot import *
from Nth_root import *

class CalculatorTest(unittest.TestCase):
    def test_add(self):
        for i in range(-9999,9999,100):
            for j in range(-9999,9999,100):
                self.assertEqual(add(i,j), i+j)
        self.assertEqual(add(0,0),0)
    
    def test_sub(self):
        for x in range(-9999,9999,100):
            for i in range(-9999,9999,100):
                self.assertEqual(subtract(x,i), x-i)

    def test_multiply(self):
        for x in range(-9999,9999,50):
            for y in range(-9999,9999,50):
                self.assertEqual(multiply(x,y), x*y)

    def test_divide(self):
        for x in range(-9999,9999,50):
            for y in range(-9999,9999,50):
                self.assertEqual(divide(x,y), x/y)
    
    def test_mod(self):
        for x in range(-9999,9999,50):
            for y in range(-9999,9999,50):
                self.assertEqual(mod(x,y), x%y)

    def test_intDivide(self):
        for x in range (-9999,9999,50):
            for y in range(-9999,9999,50):
                self.assertEqual(whole(x,y), x//y)

    def test_power(self):
        for x in range(-5,-1,1):
            for y in range(-5,5,1):
                #print(x,y,-5**-5,power(-5,-5))
                self.assertEqual(power(x,y), x**y)
        for x in range(1,5,1):
            for y in range(-5,5,1):
                #print(x,y,-5**-5,power(-5,-5))
                self.assertEqual(power(x,y), x**y)

    def test_factorial(self):
        for i in range(0,10,10):
            self.assertEqual(fact(i), math.factorial(i))
    
    def test_sqrt(self):
        for x in range(0, 999999,50):
            self.assertEqual(squareroot(x), sqrt(x))
    
    def test_nroot(self):
        for x in range(-5,5, 5):
            for y in range(-5,-1, 1):
                self.assertEqual(nth_root(x,y),-(x**(1.0/-y)))
                #python cant use negative when fractional power
if __name__ == '__main__':
    unittest.main()    

#https://jeffknupp.com/blog/2013/12/09/improve-your-python-understanding-unit-testing/
