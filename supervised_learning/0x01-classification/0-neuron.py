#!/usr/bin/env python3
"""
0-neuron.py
"""
import numpy as np


class Neuron:
    """Neuron"""
    def __init__(self, nx):
        """Initializes the data."""
        if type(nx) != int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        self.W = np.random.normal(loc = 0.0, scale = 1.0, size = (1, nx))
        self.b = 0
        self.A = 0
