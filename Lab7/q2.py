# File: q2.py
# Author: Yuhao Ye
# Date: 07/18/2020
# Section: 529006730
# E-mail: yeyuhao1234@tamu.edu
# Description:
# Calculates the position of a car moving in a 2D-plane given the list of movements that should be executed
# order.
print('**************************************************************************')

flag = True
while flag:
  try:
     current_x = 0.0
     current_y = 0.0
     operation = input(f'Get movements :').split(',')
     for ins in operation:
         line  = ins.split()
         direction  =  line[0]
         units = float(line[1])
         if direction  == 'up' or direction == 'down':
             if direction == 'up':
                 current_y += units
             else:
                 current_y -= units
         else:
             if direction =='left':
                 current_x -= units
             else:
                 current_x += units
     flag = False
  except ValueError:
      print(f'Invalid Input, please enter again')
      print()
print()
print(f'Current Position is : x = {current_x}, y = {current_y}')
print('**************************************************************************')