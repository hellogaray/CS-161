# Author: Leonel Garay
# Date: 11/04/2019
# Description: Takes a list of numbers as parameter and gets the median.


def find_median(num_list):
    """Takes a list of numbers as parameter and gets the median"""
    num_list.sort()
    list_size = len(num_list)
    if list_size % 2 == 0:  # if number is odd then calculate median this way
        first_position = list_size / 2  # gets the first middle count based on size of list
        second_position = first_position - 1  # gets the second count number based on size of list
        even_calculation = (num_list[int(first_position)] + num_list[int(second_position)]) / 2  # calculates median
        return even_calculation
    else:  # if number is even then calculate median this way
        odd_calculation = (list_size + 1) / 2  # gets the middle count based on size of list
        odd_number = num_list[int(odd_calculation) - 1]  # median calculation
        return odd_number
