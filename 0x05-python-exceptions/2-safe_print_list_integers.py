#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    '''
    safe_print_list_integers - prints the first x elements of a list
    and only integers.

    Args:
        @my_list: list of elements.
        x: The number of elements to print from my_list.

    Returns:
        The number of elements printed.

    Author:
        Felix Obianozie
    '''
    count = 0
    if (x > 0):
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end="")
                count = count + 1
            except (TypeError, ValueError):
                continue
    print()
    return count
