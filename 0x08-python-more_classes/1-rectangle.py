#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Representation of a rectangle"""
    def __init__(self, width=0, height=0):
        """to initialize the rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """the getter for the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """the setter for the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """the getter to the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """the setter to the height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
