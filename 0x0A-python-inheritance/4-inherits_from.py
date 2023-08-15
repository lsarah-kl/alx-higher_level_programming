#!/usr/bin/python3
"""Definition of an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj : The object to check.
        a_class : The class to match the type of obj to.
    Returns:
        If sucess - True.
        Else - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
