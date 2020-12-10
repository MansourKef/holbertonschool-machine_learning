#!/usr/bin/env python3
"""
10-matisse.py
"""


def poly_derivative(poly):
    """
    poly_derivative
    """
    if len(poly) == 0:
        return None

    if len(poly) == 1:
        return [0]

    result = []
    for i in range(1, len(poly)):
        result.append(poly[i] * i)
    return result
