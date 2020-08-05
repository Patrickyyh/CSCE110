# This function return the max number in the list
def find_max(numbers):
   max = numbers[0]
   for i in range(1,len(numbers)):
       if numbers[i] > max:
           max = numbers[i]
   return max



def searching_function(numbers,target):
    """Linear searching"""
    """Some other way to search something """
    for i in range(len(number)):
        if numbers[i] == target:
            return i

    return -1





number = [1,2,3,4,14,21,23,12]
result = searching_function(number,23)
if result == -1:
    print('Sorry we cannot find the target in the list ')
else:
    print(result)

print(find_max(number))

