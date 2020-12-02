#!/usr/bin/env python3
"""
np_cat
"""


import numpy as np


def np_cat(mat1, mat2, axis=0):
    """
    np_cat
    """
    if not axis:
        return np.vstack((mat1, mat2))
    return np.hstack((mat1, mat2))
