numbers = [2, 4, 5, 8]
user_input = input()
while user_input != 'end':
    try:
        # possible ValueError
        divisor = int(user_input)
        if divisor > 20:
            # possible NameError
            result = compute(result)
        elif divisor < 0:
            # Possible IndexError
            result = numbers[divisor]
        else:
            # possible ZeroDivisionError
            result = 20 // divisor          # // truncates to an integer
        print(result, end=' ')
    except (ValueError, ZeroDivisionError):
        print('r', end=' ')
    except (NameError, IndexError):
        print('s', end=' ')
    user_input = input()
print('OK')