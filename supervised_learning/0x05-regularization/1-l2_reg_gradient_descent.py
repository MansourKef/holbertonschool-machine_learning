#!/usr/bin/env python3
"""mod"""

import numpy as np


def l2_reg_gradient_descent(Y, weights, cache, alpha, lambtha, L):
    """function"""
     weights_t = weights.copy()
     m = Y.shape[1]
     for i in reversed(range(L)):
         if i == L - 1:
             dZ = cache['A{}'.format(i + 1)] - Y
             dW = (np.matmul(dZ, cache['A{}'.format(i)].T)) / m
         else:
             dZa = np.matmul(weights_t['W{}'.format(i + 2)].T, dZ)
             dZb = 1 - cache['A{}'.format(i + 1)]**2
             dZ = dZa * dZb
             dW = (np.matmul(dZ, cache['A{}'.format(i)].T)) / m
        dW_reg = dW + (lambtha / m) * weights_t['W{}'.format(i + 1)]
        db = np.sum(dZ, axis=1, keepdims=True) / m
        weights['W{}'.format(i + 1)] = weights_t['W{}'.format(i + 1)] \
            - (alpha * dW_reg)
        weights['b{}'.format(i + 1)] = weights_t['b{}'.format(i + 1)] \
            - (alpha * db)
