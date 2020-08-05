"""Write a function that gets a list as input and returns a new list that contains
all the numbers of the first list minus all the duplicates."""
def reduce_duplicates(numbers):
    new_numbers = list()
    for i in numbers:
        if i not in new_numbers:
            new_numbers.append(i)

    return new_numbers



numbers = [1,2,3,4,4,4,5,5]
print(reduce_duplicates(numbers))