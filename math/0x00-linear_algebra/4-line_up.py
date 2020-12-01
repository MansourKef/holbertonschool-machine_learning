#!/usr/bin/env python3
def add_arrays(arr1, arr2):
        """
        add_arrays
        """
        if len(arr1) != len(arr2):
                return None
        return [x + y for x, y in zip(arr1, arr2)]
