# -*- coding: utf-8 -*-
"""
Quick unittest investment calculator
"""

from Calculator import Calculator
import unittest

class Test_Calculator(unittest.TestCase):
    
    def setUp(self):
        self.first = Calculator(10000)
        
    def test_add_interest(self):
        self.assertTrue('Your investment has grown to 16105', self.first.add_interest())

 
if __name__ == "__main__":
    unittest.main()   
    

    