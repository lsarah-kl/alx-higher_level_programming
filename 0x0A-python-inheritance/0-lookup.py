#!/usr/bin/python3
"""Definition of an object attribute lookup function."""


def lookup(obj):
    """Returns  list of the object's available attributes."""
    return (dir(obj))
