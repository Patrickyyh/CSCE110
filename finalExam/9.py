import math
def mask():
    """use or to set the mask """
    mask = 0b101010

def bit_rotate(n,m,d):
    binary = bin(n)[2:]
    binary_list = list(binary)
    temp_list = ["0"]*len(binary_list)

    if d == True:
       for i in range(len(binary_list)):
           if binary_list[i] == "1":
               if i + m > (len(binary_list)-1):
                   temp_list[i+m - len(binary_list)] = "1"
                   temp_list[i] = "0"
               else:
                   temp_list[i+m] = "1"
                   temp_list[i]  = "0"
    else:
       for i in range(len(binary_list)):
           if binary_list[i] == "1":
               if i - m <0:
                   temp_list[i-m+len(binary_list)] = "1"
                   temp_list[i] = "0"
               else:
                   temp_list[i-m] = "1"
                   temp_list[i] = "0"




    result = ""
    for number in temp_list:
        result += number
    print(result)
    return int(result,2)



print(bit_rotate(17,2,False))