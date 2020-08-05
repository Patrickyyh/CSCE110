import sys

numbers = [3,14,234,3,'pi',9,0,-1]
for n in numbers:
 try:
    inverse = 1/n
    print(f'The inverse of {n} is {inverse}')

 except  (TypeError,ValueError) as e:
     print(f'The error is {e}')
     print(f'The error is {sys.exc_info()[0]}')
 except ZeroDivisionError as e:
     print(f'The error is {e}')
     print(f'The error is {sys.exc_info()[0]}')
 finally:
     print(f'Out of the exception\n\n')