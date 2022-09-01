#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    """
    multiply_by_2 - function that returns a new dictionary with all values
    multiplied by 2

    Prototype:
    def multiply_by_2(a_dictionary):

    Approach:
    Dictiornary comprehension

    Author:
    Felix Obianozie
    """

    # Using dictionary comprehension
    new_dict = {x: (a_dictionary[x]**2) for x in a_dictionary}
    return new_dict
