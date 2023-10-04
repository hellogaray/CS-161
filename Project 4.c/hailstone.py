# Author: Leonel Garay
# Date: 10/22/2019
# Description: Returns the count for a hailstone sequence from a positive integer.


def hailstone(num):
    """Returns the count for a hailstone sequence from a positive integer, count starts at 1."""
    count = 0
    while num > 1:
        if num % 2 == 0:
            num = num / 2
        elif num % 2 != 0:
            num = (num * 3) + 1
        count += 1
    return count
