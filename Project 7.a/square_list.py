# Author: Leonel Garay
# Date: 11/06/2019
# Description: Function that takes as a parameter a list and replaces each value with the square of that value.


def square_list(par_list):
    """Returns each value in the list as **2 that value"""
    list_position = 0
    for num in par_list:
        num = num ** 2
        par_list[list_position] = num  # decides where to add the new num
        list_position += 1  # moves 1 position
    return par_list
