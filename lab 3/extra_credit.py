number = input("Enter integers: ").split(",")
intege_number= []
number_count = 0
print()
for numbers in number:
    intege_number.append(int(numbers))


for numbers in intege_number:
    if numbers % 7 ==0:
        number_count +=1

print(f"You have entered {number_count} numbers divisible by 7 and {len(intege_number) - number_count} are not. ")
