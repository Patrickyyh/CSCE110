# File: extra_credit.py
# Author: Yuhao Ye
# Date: 07/18/2020
# Section: 529006730
# E-mail: yeyuhao1234@tamu.edu
# Description:
#  Computate the Euclidean distance between two pointes. Write a function that calculates the distance .
import math
def distance(list_p1 , list_p2):
    square_total= 0
    for x in range(len(list_p2)):
        square_total += math.pow(list_p1[x] - list_p2[x],2)
    return math.sqrt(square_total)




def main():
    cordinate_list = input('Enter points (x1 x2 y1 y2 ...): ').split()
    p1 = list()
    p2 = list()
    for x in range(len(cordinate_list)):
        if x % 2 == 0 :
           p1.append(float(cordinate_list[x]))
        else:
            p2.append(float(cordinate_list[x]))

    print('The distance between')
    print('P1: (',end = "")
    print(', '.join([str(num) for num in p1]),end = ")\n")
    print('P2: (',end = "")
    print(', '.join([str(num) for num in p2]), end = ")\n")
    print(f'is {round(distance(p1,p2),4)}')





if __name__ == '__main__':
    main()
