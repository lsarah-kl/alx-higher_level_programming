#!/usr/bin/python3
"""
    101-lazy_matrix_mul Module
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
        Multiplies 2 matrices

        Args:
            m_a: 1st matrix
            m_b: 2nd matrix

        Returns:
            the multiplication of matrices
    """
    return np.matmul(m_a, m_b)
