#!/usr/bin/python3
"""
Defines a class Rectangle
"""


class Rectangle:
    """Representes  a rectangle"""
    def __init__(self, width=0, height=0):
        """initializes the rectangle by
        setting the width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """the getter to the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """the setter for width attribute"""
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
        """the setter for height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """returns printable string representing the rectangle"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string
