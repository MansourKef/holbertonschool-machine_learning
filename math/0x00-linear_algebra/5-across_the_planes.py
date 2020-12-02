#!/usr/bin/env python3

"""
Module for add matrices.
"""


def add_matrices2D(mat1, mat2):
    """
    add_matrices2D
    """
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None

    result = [[0 for i in mat1[0]] for j in mat1]
    
    for i in range(len(mat1)):
        # iterate through columns
        for j in range(len(mat1[0])):
        result[i][j] = mat1[i][j] + mat2[i][j]
    return result
