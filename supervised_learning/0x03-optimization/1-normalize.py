#!/usr/bin/env python3


import numpy as np


def normalize(X, m, s):
    """
    function
    """
    X = (X - m) / s
    return X
