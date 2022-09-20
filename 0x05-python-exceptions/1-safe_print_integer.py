#!/usr/bin/python3
def safe_print_integer(value):
    '''
    safe_print_integer - prints value as integer.

    Args:
        @value: value to print.

    Returns:
        True if value has been correctly printed
        (it means the value is an integer). Otherwise, False.

    Author:
        Felix Obianozie
    '''
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        return False
