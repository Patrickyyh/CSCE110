def insertion_sort(numbers):
    for i in range(1,len(numbers)):
        j = i
        while j > 0 and numbers[j-1] > numbers[j]:
           temp = numbers[j]
           numbers[j] = numbers[j-1]
           numbers[j-1] = temp
           j = j-1




numbers = [10, 2, 78, 4, 45, 32, 7, 11]
print('Unsorted: ' , end = " ")
for num in numbers:
    print(str(num), end = " ")
insertion_sort(numbers)
print()
for num in numbers:
    print(str(num) , end  = " ")
