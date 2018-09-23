# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 20:39:40 2018

@author: shirhe-lyh


Test Case with a new method assertAllEquals for numpy.ndarray.
"""

import numpy as np
import unittest

class TestCase(unittest.TestCase):
    
    def assertAllEquals(self, first, second, msg=None):
        """Fail if the two objects are unequal as determined by the '=='
           operator.
        """
        if isinstance(first, np.ndarray) and isinstance(second, np.ndarray):
            if not (first == second).all():
                msg = self._formatMessage(msg, "%s != %s" %(first, second))
                raise self.failureException(msg)
        else:
            return self.assertEqual(first, second)
        
        
def main():
    """Runs all test cases."""
    unittest.main()
        
