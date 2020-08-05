from random import randint
import math
def square(number):
     return math.pow(number,2)

def add_square(number, roster):
    while True:
       roster.append(square(number))
       if(square(number > 100)):
           break
       number+=1
    print(roster)
    print(max(roster))
    print(min(roster))
    print()
    print("The list of squares is populated!")

roster= []
number = 1
add_square(roster = roster, number = number)