number  = int(input("Enter a number: "))
if(number < 1):
    print("n must be greater than 1")
else:
    for number in range(1,number+1):
        temp = float(number)
        temp_root = temp **(1/2)
        print(f'The square root of {number} is {round(temp_root,2)}')