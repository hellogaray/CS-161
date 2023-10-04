# Author: Leonel Garay
# Date: 11/05/2019
# Description: Takes a list of names and adds "Kardashian" to names that start with K.


def add_surname(list_names):
    """Takes a list of names and adds "Kardashian" to names that start with K."""
    last_name = " Kardashian"  # last name to be added
    only_k_list = [first_name + last_name for first_name in list_names if "K" in first_name]  # new list with K names
    return only_k_list
