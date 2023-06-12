#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for aux in range(x):
            print(("{:d}".format(my_list[aux])), end="")
    except Exception:
        print()
        return aux
    print()
    return x
