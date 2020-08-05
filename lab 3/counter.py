my_list = input("Enter a,b,c: ").split(",")
my_list.sort()
count = 0
temp = 0
while(True):
    temp = my_list[0]
    my_list.pop(0)
    if (len(my_list) == 0):
        break
    if temp == my_list[0]:
        count +=1


if count == 0:
    print(f'There are {count} equal numbers')
else:
    print(f'There are {count+1} equal numbers')