#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    '''
    list_division - divides element by element 2 lists.

    Args:
        @my_list_1: first list of elements.
        @my_list_2: second list of elements.
        @list_length: number of elements to divide.

    Returns:
        New list (length = list_length) with all divisions.

    Author:
        Felix Obianozie
    '''
    new_list = []
    if (list_length > 0):
        for i in range(list_length):
            try:
                result = my_list_1[i] / my_list_2[i]
            except ZeroDivisionError:
                result = 0
                print("division by 0")
            except (TypeError, ValueError):
                result = 0
                print("wrong type")
            except IndexError:
                result = 0
                print("out of range")
            finally:
                new_list.append(result)
    return new_list
