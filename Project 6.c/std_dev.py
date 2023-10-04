# Author: Leonel Garay
# Date: 11/05/2019
# Description: Calculate the Standard Deviation of all ages of people in list.


class Person:
    """Has two data members - the person's name and age."""

    def __init__(self, person_name, person_age):
        """Takes two values and uses them to initialize the data members."""
        self.name = person_name  # name is the first parameter
        self.age = person_age  # age is the second parameter


def std_dev(people_list):
    """Calculates the Standard Deviation (of a Population) of all ages"""
    sum_age = 0
    mean_age = 0
    for person in people_list:
        sum_age += person.age  # sum of all ages
    average_age = sum_age / len(people_list)  # average of all ages
    for person in people_list:
        mean_age += (person.age - average_age) ** 2  # sum of the result of (each age minus the mean) squared
    squared_mean = mean_age / len(people_list)  # mean of all squared ages
    stand_deviation = squared_mean ** (1 / 2)  # gets the standard deviation by getting the mean of all squared ages
    return stand_deviation
