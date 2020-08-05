import sys
numbers = [1,4,-6,0,3,-12]
for n in numbers:
    try:
        reciprocal = 1/n
        print(f'The reciprocal of {n} is {reciprocal}')
    except ZeroDivisionError as e:
        print(f'The error {sys.exc_info()}')
        print(f'Error infomation {e}')