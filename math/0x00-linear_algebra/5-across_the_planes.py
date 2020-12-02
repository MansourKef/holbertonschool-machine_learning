#!/usr/bin/env python3

"""
Module for add matrices.
"""


def add_matrices2D(mat1, mat2):
        """
        add_matrices2D
        """
        if len(mat1) != len(mat2):
            return None
        result = [[0, 0],
                  [0, 0,]]
        for i in range(len(mat1)):
            # iterate through columns
            for j in range(len(mat1[0])):
                result[i][j] = mat1[i][j] + mat2[i][j]
        return result
    
