#!/usr/bin/python3
""" Square definition """


class Square:
    """ Declaration of square class """

    def __init__(self, size=0) -> None:
        """
        Intializes new class

        Args:
            size: square size
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Return the area of a square
        """
        return self.__size ** 2
