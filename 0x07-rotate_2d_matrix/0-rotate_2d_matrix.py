#!/usr/bin/python3
"""
This module covers the implementation of Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D Matrix 90 degrees clockwise
    """
    # Transpose the matrix
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix[i])):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = tmp

    # Reverse each row
    for row in matrix:
        row.reverse()
