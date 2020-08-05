# File: q2.py
# Author: Yuhao Ye
# Date: 06/19/2020
# Section: 529006730
# E-mail: yeyuhao1234@tamu.edu
# Description:
#  the program will ask the user for the triangle’s height. Then, it will ask for two symbols,
#  that will be used in alternate lines to draw the triangle.


height = int(input("Height of triangle: "))
first_symbol = input("Enter the first symbol: ")
second_symbol = input("Enter the second symbol: ")
print()
for number in range(height):
    if number % 2 == 0:
       print_symbole = first_symbol
    else:
        print_symbole = second_symbol

    for j in range(height, number, -1):
        print(" ", end="")
    for j in range(0, number + 1):
        print(f'{print_symbole}', end="")

    for j in range(0, number):
        print(f'{print_symbole}', end="")
    print()
