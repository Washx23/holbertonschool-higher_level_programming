#!/usr/bin/python3
"""
document
"""


class Square:
    """Class Square"""
    def __init__(self, __size=0):
        """Square"""
        if type(__size) is not int:
            raise TypeError("size must be an integer")
        if int(__size) < 0:
            raise TypeError("size must be >= 0")
        self.__size = __size

    def area(self):
        a = self.__size * self.__size
        return a