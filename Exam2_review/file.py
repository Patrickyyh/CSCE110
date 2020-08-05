import os
import sys

try:
    with open("resource.txt",'r') as read:
        store = list()
        store = read.readlines()
        print(store)
    with open('Target.txt','x') as write:
        for line in store:
            write.write(line)

except (FileNotFoundError) as e:
    print(f'The error is {e}')
except FileExistsError as e:
    print(f'{e} occurs')
    try:
     filename = input("Enter the new name of the file ")
     with open(filename,'x') as write:
         for line in store:
            write.write(line)
    except FileExistsError as e:
        print(e)