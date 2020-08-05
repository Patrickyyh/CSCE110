
# File: q2.py
# Author: yuhao ye
# Date: 07/10/2020
# Section: 529006730
# E-mail: yeyuhao1234@tamu.edu
# Description:
# Write The function throw_darts() to estimate the value of pi


import  random
import math
def throw_darts(n):
    count = 0
    for i in range(n):
     x_value = random.uniform(-1,1)
     y_value = random.uniform(-1,1)

     distance = math.sqrt(x_value**2 + y_value**2)
     if distance <=1:
         count +=1
    return 4 * (count / n)


def main():
   amount = int(input('How many darts to throw? '))
   print(f'PI = {throw_darts(amount)}')

if __name__ == '__main__':
    main();