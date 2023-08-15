#!/usr/bin/python3
"""Definition of a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.

    Args:
        obj : The object to check.
        a_class : The class to match the type of obj to.
    Returns:
        If success - True.
        Else - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
