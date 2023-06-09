#!/usr/bin/python3


def roman_to_int(roman_string):
    if isinstance(roman_string, str) is False:
        return 0

    var = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    for i, let in enumerate(roman_string):
        aux = 0
        if i < len(roman_string) - 1:
            aux = var.get(let) >= var.get(roman_string[i + 1])
        if i == len(roman_string) - 1 or aux:
            res += var.get(let)
        else:
            res -= var.get(let)
    return res
