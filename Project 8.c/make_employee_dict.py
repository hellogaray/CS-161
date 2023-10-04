# Author: Leonel Garay
# Date: 11/13/2019
# Description: Employee class with employee information and function that creates a dictionary.


class Employee:
    """Class that has all of the employee information: name, ID_number, salary, email_address"""

    def __init__(self, name, ID_number, salary, email_address):
        self.name = name
        self.ID_number = ID_number
        self.salary = salary
        self.email_address = email_address


emp_dict = {}  # empty dictionary


def make_employee_dict(name, id_number, salary, email_address):
    """Creates a dictionary using id as key, and all of the information under the Employee class"""
    position = 0
    for var in id_number:
        emp_object = Employee(name[position], id_number[position], salary[position], email_address[position])
        emp_dict[id_number[position]] = emp_object  # Adds employee to the dictionary
        position += 1  # Moves to the following employee
    return emp_dict
