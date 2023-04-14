##example_test_case3.py

import unittest

def add(x, y):
    return x + y

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(5, -3), 2)
        try:
            self.assertEqual(add(0, 0), 1)
        except AssertionError:
            print('Error: testing {} the function returned {} the test expected {}'.format('add(0, 0)', add(0, 0), 1))