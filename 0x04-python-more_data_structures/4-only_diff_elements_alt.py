#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    # Letters in set_1 not in set_2
    diff1 = set_1 - set_2

    # Letters in set_2 not in set_1
    diff2 = set_2 - set_1

    # Return of single set of all the letters (set union)
    return diff1 | diff2
