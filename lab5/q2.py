
# File: q2.py
# Author: Yuhao Ye
# Date: 07/03/2020
# Section: 529006730(UIN)
# E-mail: yeyuhao1234@tamu.edu
# Description:
# Take two words of any length and return the letters that are shared between them

line = input("Enter two words: ").split()
print()
first_word = list(line[0])
second_word = list(line[1])
first_dict  = dict()
second_dict = dict()
same_letter= list()
for  key , value in enumerate(first_word):
     if value not in first_dict.values():
        first_dict[key]= value

for  key , value in enumerate(second_word):
     if value not in second_dict.values():
        second_dict[key] = value

for key,value_1 in first_dict.items():
    for key , value_2 in second_dict.items():
        if value_1 == value_2:
            same_letter.append(value_1)


print(f'The words {line[0]} and {line[1]} share {len(same_letter)} letters:')
for number in sorted(same_letter):
    print(number, end=" ")