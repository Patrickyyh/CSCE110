# File: q2.py
# Author: Yuhao Ye
# Date: 06/28/2020
# Section: 529006730
# E-mail: yeyuhao1234@tamu.edu
# Description:
# print the list of items and print the list without duplicate items and
#list of duplicated items
items = input("Enter the list of items: ").split()
duplicate = list()
duplicate_count = 0
print()


for x in items[:]:
    for y in items[items.index(x) + 1:]:
        if(x == y):
            temp_count = items.count(x)
            if temp_count > duplicate_count:
                duplicate_count = temp_count
            if (x in duplicate) == False:

                duplicate.append(x)

print(f'Found {duplicate_count} duplicates: ')
for item in duplicate:
    print(item , end=" ")


print()
print()


for x in items[:]:
    if x in duplicate:
        items.remove(x)

print("Items without duplicates: ")
for item in items:
    print(item,end= " ")

