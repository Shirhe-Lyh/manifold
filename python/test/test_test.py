# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 21:40:50 2018

@author: shirhe-lyh


Test for test.TestCase.
"""

import numpy as np

import test

class TestCaseTest(test.TestCase):
    """Test the function assertAllEquals."""
    
    def test_assertAllEquals_for_ndarrays(self):
        first = np.array([[1.0, 1.5, 2.0], [-1.0, -0.5, 0.0]])
        second = np.array([[1, 1.5, 2], [-1, -0.5, 0]])
        self.assertAllEquals(first, second)
        
        first = np.array([[1.0, 1.5, 2.0], [-1.0, -0.5, 0.0]])
        second = np.array([[1, 1.5, 2], [-1, -0.5, 0.1]])
        self.assertRaises(AssertionError, self.assertAllEquals, first, second)
        
    def test_assertAllEquals_for_non_ndarrays(self):
        first = [1., 2., 3.]
        second = [1., 2., 3]
        self.assertAllEquals(first, second)
        
        
if __name__ == '__main__':
    test.main()