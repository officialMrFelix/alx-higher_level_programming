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
    1.Create new list variable to hold result of all subsequent evaluations
    2.For each item (a list) in matrix,
    3.Create temp. list variable for each new item from matrix after x^2
    4.Use map function to perform exponentiation per item from matrix
    5.Append modified item from matrix to new list variable
    6.Clear temporary list variable from memory
    7.Return the newly generated list

    Author:
    Felix Obianozie
    '''

    # 1
    newList = []

    # 2
    for i in matrix:
        # 3 & 4
        tempList = list(map(lambda x: x**2, i))

        # 5
        newList.append(tempList)

    # 6
    del tempList

    # 7
    return newList
