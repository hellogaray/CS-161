# Author: Leonel Garay
# Date: 10/08/2019
# Description: Converts entered amount to number of cents

print("Please enter an amount in cents less than a dollar.")
amount = int(input())
print("Your change will be:")
quater = amount//25
print("Q:", quater)
dime = (amount - (quater * 25))//10
print("D:", dime)
nickle = (amount - ((quater * 25) + (dime * 10)))//5
print("N:", nickle)
penny = (amount - ((quater * 25) + (dime * 10) + (nickle * 5)))//1
print("P:", penny)