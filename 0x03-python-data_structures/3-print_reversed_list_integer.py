#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        index = len(my_list) - 1
        for i in my_list:
            print("{:d}".format(my_list[index]))
            index -= 1
