# Author: Leonel Garay
# Date: 10/24/2019
# Description: Takes two positive integers as parameters and returns the product of those two numbers


def multiply(multiplicand, multiplier):
    """takes two positive integers as parameters and returns the product of those two numbers by addition only """
    if multiplier == 1: # if multiplier is 1 returns multiplicand
        return multiplicand
    return multiply(multiplicand, multiplier - 1) + multiplicand
