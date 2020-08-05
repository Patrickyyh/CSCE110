# File: q1.py
# Author: Yuhao Ye
# Date: 06/28/2020
# Section: 529006730
# E-mail: yeyuhao1234@tamu.edu
# Description:
# choose any two items to buy at a store given a certain budget.
# and print out the leftover
item = input("Enter the prices of store items: ").split()
budget = float(input("Enter your budget: "))
print()
item_number = [float(n) for n in item]
for item in item_number:
    for item_2 in  item_number[item_number.index(item)+1:len(item_number)]:
        total_price = item_2 + item
        if (total_price <= budget ):
            print(f'You can buy item {item_number.index(item)+1} and item {item_number.index(item_2) + 1 } with ${ round(budget-total_price,2)} leftover.')

