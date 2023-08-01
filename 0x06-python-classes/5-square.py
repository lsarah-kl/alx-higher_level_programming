#!/usr/bin/python3
""" Square definition """


class Square:
    """ Declaration of a square class """

    def __init__(self, size=0) -> None:
        """
        Intializes new class

        Args:
            size: square size
        """
        self.size = size

    @property
    def size(self):
        """ Gets the attribute to be used in class """
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
        """ Calculates square area """
        return self.__size ** 2

    def my_print(self):
        """ Prints  square with # in stdout """
        if self.__size == 0:
            print()
        else:
            integer = 0
            while integer < self.__size:
                number = 0
                while number < self.__size:
                    print("{}".format("#"), end='')
                    number += 1
                print()
                integer += 1
