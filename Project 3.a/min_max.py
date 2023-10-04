# Author: Leonel Garay
# Date: 10/11/2019
# Description: Ask user number of integers, user inputs integers, and displays the largest and smallest of those numbers.
#Ask user for amount of numbers to be used.'
min_number = 1000000000000000000
max_number = -1000000000000000000
print("How many integers would you like to enter?")
num_int = int(input())
#Ask user for the numbers to be used.
if num_int == 1: #Use "integer" if the number is 1.
    print("Please enter", num_int, "integer.")
else: #If the number is greater than 1, use "integers".
    print("Please enter", num_int, "integers.")
for val in range(1, num_int + 1):
    all_numbers = int(input())
    if all_numbers <= min_number: #if input is <= than min_number then it saves until a smaller number is present
        min_number = all_numbers
    if all_numbers >= max_number: #if input is >= than max_number then it saves until a bigger number is present
        max_number = all_numbers
print("min:", min_number)
print("max:", max_number)

