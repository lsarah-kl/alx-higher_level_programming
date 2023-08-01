#!/usr/bin/python3
""" Square definition """


class Square:
    """ square representation """

    def __init__(self, size=0) -> None:
        """
        Intializes new class 

        Args:
            size : square size
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
