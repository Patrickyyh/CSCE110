# File: q5.py
# Author: Yuhao Ye
# Date: 06/13/2020
# Section: 529006730(UIN)
# E-mail: yeyuhao1234@tamu.edu
# Description:
# Take in the cost of the gas for the last five months and
#print out the average cost with two digits after the decimal point.

cost = input("Enter gas cost: ").split()
total = 0;
print()
for numer_cost in cost:
    total += float(numer_cost)

total  = round(total/5,2)
total = "{:.2f}".format(total)

print(f"On average, you will spend ${total} per gallon for gas this month.")