#!/usr/bin/python3
"""Definition of a square to output"""


def print_square(size):
    """
        Prints a square with the character '#'

        Args:
            size: square length"""
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
