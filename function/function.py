# re-usability of the function
# Functions can be part pf the language(built in functions)
#user-defined by the users(user_defined functions.)
import math
def absolute_value(number):
     if number >=0:
         return number
     else:
         return -number


def hypotenuse(a,b):
    c = math.sqrt(math.pow(a,2)+math.pow(b,2))
    print(f'The hypotenuse of a triangle of side {a} and side {b} is {c}')

def arighmetic(side_1 ,side_2):
    a = absolute_value(side_1)
    b = absolute_value(side_2)
    hypotenuse(a,b)

#number =int(input("Enter a number"))
#print(absolute_value(number))

def main(side_1,side_2):
    a = absolute_value(side_1)
    b = absolute_value(side_2)
    hypotenuse(a,b)

side_1 = float(input("Enter the first side"))
side_2 =float(input("Enter the seconde side"))
if __name__ == "__main__":
 # only run the following instruction if the program is executed as standalone
    main(side_1,side_2)