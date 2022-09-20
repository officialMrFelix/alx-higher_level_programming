#!/usr/bin/python3
def safe_print_division(a, b):
    '''
    safe_print_division - divides 2 integers and prints the result.

    Args:
        @a (int): numerator
        @b (int): denominator

    Returns:
        Result of division. Otherwise, None.

    Author:
        Felix Obianozie
    '''
    try:
        result = a / b
    except Exception:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
