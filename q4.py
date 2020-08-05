# File: q4.py
# Author: Yuhao Ye
# Date: 06/13/2020
# Section: 529006730(UIN)
# E-mail: yeyuhao1234@tamu.edu
# Description:
# Ask user for the coefficients a ,b, c and print the euation in the form of ax^2 + bx +c = 0
# Calculate and print the value of the discriminant d
# print the soluiton to the equation and solution rounded to two digits after the decimal point

number = input("Enter the coefficients a, b, c: ").split()
print()
a = float(number[0])
b = float(number[1])
c = float(number[2])
disc = b**2 - 4 * a * c

print(f'The quadratic equation is: {a}x^2 + {b}x + {c} = 0')
print(f'The discriminant d is: {disc}')




if disc > 0:
    solution1 = (-b + (b**2 -4 * a * c)**(1/2))/(2*a)
    solution2 = (-b - (b**2 -4 * a * c)**(1/2))/(2*a)
    print(f'First solution: {solution1}, second soluion: {solution2}')
    print(f'First solution rounded: {round(solution1,2)}, second solution rounded: {round(solution2,2)}')


elif disc < 0:
    solution1 = (-b + (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)

    solution2 = (-b - (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)


    print(f'First solution: {solution1}, second soluion: {solution2}')
    solution1_imag = round(solution1.imag,2)
    solution1_real = round(solution1.real,2)
    solution2_imag = round(solution2.imag,2)
    solution2_real = round(solution2.real,2)
    solution1_real = "{:.2f}".format(solution1_real)
    solution2_real = "{:.2f}".format(solution2_real)

    solution2_imag = "{:.2f}".format(solution2_imag)
    solution1_imag = "{:.2f}".format(solution1_imag)


    print(f'First solution rounded: {solution1_real}+{ solution1_imag}j, second solution rounded: {solution2_real}{solution2_imag}j')



else:
    soluion  = (-b)/(2 * a)
    print(f'The only solution is {soluion}')
    print(f'The only solution rounded is {round(soluion,2)}')



