#!/usr/bin/env python3
"""module"""


def early_stopping(cost, opt_cost, threshold, patience, count):
    """function"""
    if (opt_cost - cost) <= threshold:
        if count + 1 >= patience:
            return True, count + 1
        else:
            return False, count + 1
    else:
        return False, 0
