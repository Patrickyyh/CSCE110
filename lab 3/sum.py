sum = 0
numbers = [[2, 4, 1], [8, -4], [12, 6, 7], [35], [-1, 2, 0, 6]]
for number in numbers:
    for digit in number:
        sum = digit + sum


print(f"The sum of all number: {sum}")