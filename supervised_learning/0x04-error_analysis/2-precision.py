#!/usr/bin/env python3
"""
mod
"""


import numpy as np


def precision(confusion):
    """
    function
    """
    return np.divide(confusion.diagonal(),
                     np.sum(confusion, axis=0))
