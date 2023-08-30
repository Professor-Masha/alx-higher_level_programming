#!/usr/bin/python3
"""Def a class Sqr"""


class Square:
    """Rep a square"""

    def __init__(self, size):
        """Init a new sqr

        Args:
            size (int): Size of the new sqr
        """
        self.size = size

    @property
    def size(self):
        """Set the current size of the sqr"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the sqr"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # char"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
