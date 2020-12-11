#!/usr/bin/env python3
"""
9-sum_total.py
"""

def summation_i_squared(n):
    """
    9-summation_i_squared.py
    """
    if type(n) != int or n < 1:
        return None
    result = 0
    for i in range(1, n+1):
        result = result + i*i
    return (n * (n + 1) * (2 * n + 1)) // 6
