##calculator_test.py

import calculator #load in the module that we want to test
import unittest #import the built-in unittest module from python which contains the methods we will neeed


class TestCalculator(unittest.TestCase): 
  #create a class called TestCalculator which inherits attributes from the unittest.TestCase class

    def test_addition(self): #write a test for each of the functions in the calculator module to ensure it is working propertly
        result = calculator.add(5, 3)
        self.assertEqual(result, 8)

    def test_subtraction(self):
        result = calculator.subtract(5, 3)
        self.assertEqual(result, 2)

    def test_multiplication(self):
        result = calculator.multiply(5, 3)
        self.assertEqual(result, 15)

    def test_division(self):
        result = calculator.divide(10, 2)
        self.assertEqual(result, 5.0)
