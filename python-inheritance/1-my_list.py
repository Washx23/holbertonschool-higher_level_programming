#!/usr/bin/python3
"""
1. My list
"""


class MyList(list):
    """MyList"""
    def print_sorted(self):
        """print_sortet"""
        a = list.copy(self)
        a = sorted(a)
        print(a)
