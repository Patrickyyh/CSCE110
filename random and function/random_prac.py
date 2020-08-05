from random import *
secret_number = randint(1,100)
number = int(input("Enter a number betwee 1 and 100: "))
count = 1
while number != secret_number:
       if number >secret_number:
           print(f'{number} is too high')
       elif number < secret_number:
           print(f'{number} is too low')

       number = int(input("Enter a number betwee n1 and 100: "))
       count +=1

print(f'You guess the secret number {secret_number} in {count} attempts')