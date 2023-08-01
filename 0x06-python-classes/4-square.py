#!/usr/bin/python3
""" Square definition """


class Square:
    """ Definition of a square class """

    def __init__(self, size=0) -> None:
        """
        Intializes new class

        Args:
            size: square size
        """
        self.size = size

    @property
    def size(self):
        """ Gets the attribute to use in class """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Return the area of a square """
        return self.__size ** 2
