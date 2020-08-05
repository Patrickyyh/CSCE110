## 1 dollar = 4 quater
## 1 dollar = 10 dimes
## 1 dollar = 20 nickels
## 1 dollar =  100 pennies


# A penny is worth 1 cent.
# A nickel is worth 5 cents.
# A dime is worth 10 cents.
# A quarter is worth 25 cents.

#dollar = float(input("Enter the change amount: "))
#cents = int(dollar * 100)
#
### dollar
#dollar_amount = int(cents / 100)
#cents = cents - dollar_amount * 100
#
## quarter
#quarter_amount = int(cents / 25)
#cents   = cents - quarter_amount * 25
#
##dimes
#dime_amount = int( cents / 10)
#cents   = cents - dime_amount  * 10
#
#
##nickels
#nickels_amount = int (cents / 5)
#cents = cents - nickels_amount *5
#
###
#penny_amount = cents
#
#if (dollar_amount != 0):
#    print("Dollar : ", dollar_amount)
#
#if (quarter_amount != 0 ):
#    print("Quarter : " ,quarter_amount)
#
#if(dime_amount != 0 ):
#    print("Dimes: " , dime_amount)
#
#if(nickels_amount != 0 ):
#    print("Nickels: " , nickels_amount)
#
#
#
#
#phrase = "Python String"
#print ( phrase [3:5]) ## ho
#print ( phrase [7:])   ## String space
#print ( phrase [:6])  ##Python
#print ( phrase [7: -4]) ## St
#
#
#stop_sign = int(input("Please enter an number:"))
#total = 0
#for number in range(stop_sign):
#    total  = total + number
#
#print('The result is {}'.format(total))
#


line_number = input("Enter a string of position intergers : ").split()
number_version = []
for number in line_number:
     number_version.append(int(number))

for number1 in number_version:
    for number2 in range(number1):
        print("*", end ="")
    print()
