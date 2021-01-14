#!/usr/bin/env python3


import numpy as np


def normalization_constants(X):
    """
    function
    """
    mean = X.mean(axis=0)
    std = X.std(axis=0)
    return mean, std
