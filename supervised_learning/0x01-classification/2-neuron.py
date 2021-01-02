#!/usr/bin/env python3
"""
2-neuron.py
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
        self.__W = np.random.normal(loc=0.0, scale=1.0, size=(1, nx))
        self.__b = 0
        self.__A = 0

        @property
        def W(self):
            """Get Function"""
            return self.__W

        @property
        def b(self):
            """Get Function"""
            return self.__b

        @property
        def A(self):
            """Get Function"""
            return self.__A

        def forward_prop(self, X):
            """forward_prop Function"""
            Z = np.matmul(self.__W, X) + self.__b
            self.__A = 1.0 / (1.0 + np.exp(-Z))
            return self.__A
