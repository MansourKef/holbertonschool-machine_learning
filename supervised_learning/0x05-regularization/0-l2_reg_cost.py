#!/usr/bin/env python3
"""
mod
"""


import numpy as np


def l2_reg_cost(cost, lambtha, weights, L, m):
    """
    funct    """
    A = 0
    for i in range(L):
        weight = weights['W{}'.format(i+1)]
        A += np.linalg.norm(weight)
    RegCost = cost + (lambtha/(2*m))*A
    return RegCost
