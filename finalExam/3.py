
import random as random
"""
Length = 10
At least 2 capital letters, at least 2 small letters and at least 2 numbers.


"""
def generate_password():
        new_password = ""
        numbers = [0,1,2,3,4,5,6,7,8,9]
        capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        small  = capital.lower()
        print(small)
        for i in range(0,2):
            new_password = new_password + capital[random.randint(0,25)]
            new_password = new_password + small[random.randint(0,25)]
            new_password = new_password + str(numbers[random.randint(0,9)])
        for i in range(0,4):
            random_number = random.randint(0,2)
            if random_number == 0:
                nenew_password = new_password + capital[random.randint(0,25)]
            elif random_number == 1:
                new_password = new_password + small[random.randint(0,25)]
            else:new_password = new_password + str(numbers[random.randint(0,9)])
        return new_password




print(generate_password())