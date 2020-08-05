def buble_sort(numbers):
    """This function sort a list using a bubble sort"""
    n  = len(numbers)
    for i in range(n):
        for j in range(n-i-1):
            if numbers[j] > numbers[j+1]:
                """swap the number"""
                print(f'checking the statue of bubles')
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp





def main():
    numbers = input("please enter a list of the number").split()
    buble_sort(numbers)
    print(f'The sort list is {numbers}')


main()