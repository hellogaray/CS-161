# Author: Leonel Garay
# Date: 10/11/2019
# Description: User input integer, prints a list of all positive integers that divide the number evenly.
user_int = int(input("Please enter a positive integer: ")) #Ask user for the int to be used.
number = 2 #establish number as 2 since we want to avoid 1 as a result
if user_int == 1:
    print("Only possible answer is excluded from results.")
else:
    print("The factors of", user_int, "are:")
while number < user_int: #stop once number gets to user_int since we want to avoid itself as a result
    if user_int % number == 0:
        print(number) #print the number if equation = 0
        number = number + 1
    else: # if equation !=0 then move to the following number and repeat loop
        number = number + 1
