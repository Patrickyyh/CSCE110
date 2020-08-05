#check
#make sure that the entry is a 3-digit number:
number = int(input("Please enter the number : "))
if(number / 100 >= 1) and (number / 100 < 10):
    print("Yes, this is the 3 digit number .")
else:
    print("This is not the 3 digit number.")


#second version
number = input("Please enter the number: ")
is_three_digit = (len(number == 3))# boolean
if is_three_digit == True:
    print("Yes, this is the 3 digit number .")
else:
    print("This is not the 3 digit number.")


digit1 = int(number[0])
digit3 = int(number[2])
digit_offset = (digit1 - digit3 >= 2) # boolean

if(is_three_digit and digit_offset):
    #
    #  execute the following things:
    #

