# File: q3.py
# Author: Yuhao Ye
# Date: 06/19/2020
# Section: 529006730
# E-mail: yeyuhao1234@tamu.edu
# Description:
#  This progrram is for simulating a baseball game


first_team  = input("Enter team one's name: ")
second_team = input("Enter team two's name: ")
first_point = 0
second_point = 0
print()
inning_count = 1
while(True):
    current_firstPoint = int(input(f"Top of inning {inning_count}: "))
    current_secondPoint = int(input(f"Top of inning {inning_count}: "))
    first_point += current_firstPoint
    second_point +=current_secondPoint
    inning_count +=1
    print(f'Score: {first_point}-{second_point}')
    if inning_count >4 and abs(first_point - second_point) >= 10:
      break
    elif inning_count  >10 :
        break



print()
if first_point > second_point:
    print(f'The {first_team} win! {first_point} to {second_point}')
elif first_point < second_point:
    print(f'The {second_team} win! {second_point} to {first_point}')



