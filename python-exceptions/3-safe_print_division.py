#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a // b
        print("Inside result: {}".format(float(result)))
    except Exception:
        print("Inside result: {}".format(None))
        return None
    finally:
        aux = 0
    return float(result)
