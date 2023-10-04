# Author: Leonel Garay
# Date: 10/21/2019
# Description: Calculates the Fibonacci sequence.


def fib(num):
    """Takes num and calculates the results in the Fibonacci sequence, if num = 1 or 2 then returns 1 for both"""
    if num == 1:
        return 1
    elif num == 2:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)
