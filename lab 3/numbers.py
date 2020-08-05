number_list = input("Enter numbers: ").split()
print(f"Count of numbers: {len(number_list)}")
even_count = 0
odd_count = 0
sum_list = 0
digit_list = []
for number in number_list:
    if int(number) % 2 ==0:
        even_count +=1
    else:
        odd_count +=1
    sum_list += int(number)
    digit_list.append(int(number))


print(f"Even numbers: {even_count}")
print(f'Odd numbers: {odd_count}')
print(f'Sum of numbers: {sum_list}')
print(f'Highest number: {max( digit_list)}')
print(f'Lowest number: {min( digit_list)}')