#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Representation of a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializing the rectangle by
        setting the width and height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """prints a string when we delete instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """the getter to the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """the setter for the width attribute"""
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
        """the setter for the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """returns printable string rectangle representation"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join(str(self.print_symbol) * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        """returns a string representation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
