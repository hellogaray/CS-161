# Author: Leonel Garay
# Date: 11/06/2019
# Description: Reverses the order of the values on a list.


def reverse_list(par_list):
    """Reverses the order of the values on a list."""
    list_length = len(par_list)  # Finds the length of the list to help define an end point.
    for var in range(list_length):
        position = list_length - var  # Defines what the current position is.
        par_list.append(par_list[position - 1])  # Appends that var to the end of the list.
        del par_list[position - 1]  # Removes the appended var from the list.
    return par_list
