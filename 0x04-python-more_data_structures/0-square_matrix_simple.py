#!/usr/bin/python3


def square_matrix_simple(matrix=[]):

    '''
    square_matrix_simple: function that computes the square value of all
    integers of a matrix

    Prototype:
    def square_matrix_simple(matrix=[]):

    Return:
    a new matrix:Same size as matrix. Original matrix is not modified

    Approach:
    Using list comprehension, for every item in matrix called x (which is
    assumed would be a list), return x. Then within each returned x perform
    y**2 for every item therein called y.

    Author:
    Felix Obianozie
    '''

    # Using list comprehension
    newList = [[y**2 for y in x]for x in matrix]

    # Return the newly generated list
    return newList
