# File: q2.py
# Author: Yuhao Ye
# Date: 07/25/2020
# Section: 529006730
# E-mail: yeyuhao1234@tamu.edu
# Description:
#  adds numbers together in binary. The user will be prompted to enter integers to be added and
#  the program will output the addition result in binary.




import math
# converts an integer to binary
def toBinary(integer):
    binary = ""
    while integer > 0 :
     binary = binary + str(integer % 2)
     integer = integer // 2
    return binary[::-1]




# takes two binary strings and add them together

def binaryAdd(bin_first , bin_second):
    position = max(len(bin_first) , len(bin_second))

    bin_first = bin_first.zfill(position)
    bin_second =   bin_second.zfill(position)
    result = list()
    hold = '0'
    for number in range(len(bin_second)-1,-1,-1):
        if bin_second[number] == bin_first[number] and bin_first[number] == '1':
            if hold == "0":
             result.insert(0,"0")
             hold = "1"
            else:
                result.insert(0,"1")
                hold = "1"
        elif bin_second[number] == bin_first[number] and bin_first[number] == '0':
            if hold == "1":
              result.insert(0,"1")
              hold = "0"
            else:
              result.insert(0,"0")
        else:
            if hold == "1":
              result.insert(0,"0")
              hold  = "1"
            else:
                result.insert(0,"1")
    if (hold == "1"):
        result.insert(0,"1")
    return ("").join(result)




data = input('Enter integers to be added: ').split()
data_int= list([int(n) for n in data])
data_binay = list([ toBinary(n) for n in data_int])
result = "0"
for binay in data_binay:
    result = binaryAdd(result,binay)
print()
print(f"The sum is {result}")

