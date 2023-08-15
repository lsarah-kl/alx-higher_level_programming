#!/usr/bin/python3
"""Definition of a class-checking function."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.

    Args:
        obj : The object to check.
        a_class : The class to match the type of object to.
    Returns:
        If success - True.
        Else - False.
    """
    if type(obj) == a_class:
        return True
    return False
