##example_test_case.py

import unittest

def add(x, y):
    return x + y

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(5, -3), 2)
        self.assertEqual(add(0, 0), 0)
