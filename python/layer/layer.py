# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 20:15:03 2018

@author: shirhe-lyh


Base layer definition for neural networks.
"""

import numpy as np

class Layer(object):
    "Abstract class for layer's operation."""
    
    def __init__(self,
                 activation_fn=None,
                 weights_initializer=None,
                 biases_initializer=None,
                 weights_regularizer=None,
                 biases_regularizer=None,
                 reuse=None,
                 trainable=True,
                 scope=None):
        """Constructor.
        
        Args:
            activation_fn: Activation function. Set it to None to maintain a
                linear activation.
            weights_initializer: An initializer for weights. If None, the
                defualt initializer will be used.
            biases_initializer: An initializer for bias vector. If None, the
                default initializer will be used.
        """        
        
        

