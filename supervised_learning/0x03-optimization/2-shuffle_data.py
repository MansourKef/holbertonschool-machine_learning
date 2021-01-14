#!/usr/bin/env python3


import numpy as np


def shuffle_data(X, Y):
    """
    Funct
    """
    perm = X.shape[0]
    shuff = np.random.permutation(perm)
    return X[shuff], Y[shuff]
