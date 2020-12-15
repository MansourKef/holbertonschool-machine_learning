#!/usr/bin/env python3
"""
poisson.py
"""


class Poisson:
    """
    Poisson
    """
    def __init__(self, data=None, lambtha=1.):
        """
        constructor
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = sum(data) / len(data)

    def pmf(self, k):
        """
        pmf
        """
        if k < 0:
            return 0
        if not isinstance(k, int):
            k = int(k)
        k_fact = 1
        if k != 0:
            for i in range(2, k + 1):
                k_fact = k_fact * i
        return ((self.lambtha ** (k)) *
                (2.7182818285 ** (-(self.lambtha)))) / k_fact
