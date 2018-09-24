# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 20:14:06 2018

@author: shirhe-lyh


Initializer for variables.
"""

import numpy as np


class Zeros(object):
    """Initializer that generates arrays initialized to 0."""
    
    def __init__(self, dtype=np.float32):
        self._dtype = dtype
        
    def __call__(self, shape, dtype=np.float32):
        if dtype is None:
            dtype = self._dtype
        return np.zeros(shape, dtype)