my_list = [[1,2],[3,4],[5,6]]

for row in my_list:
    count =  0
    while(count < len(row)):
        print(f'{row[count]}' , end= " ")
        count +=1
    print()


## Try to use extend method
my_secondList = [[15,16],[17,18]]
my_list.extend(my_secondList)
print()



for row in enumerate(my_list):
    count =  0
    while(count < len(row)):
        print(f'{row[count]}' , end= " ")
        count +=1
    print()


print()


judge = False

target   =  int(input("Please enter an element you wanna find in the list"))


my_thirdList = [[1,2],[7,4],[5,6]]
for count , item in enumerate(my_thirdList):
    for element in item:
        if (element == target):
            judge = True
            break

    if(judge == True):
      print(f'Congratulations! , we found your element, it is in positon ')
      break
else: ## if there is break, it will skip the conditon else
    print("We are run out of the element in the lise , we cannot find your element in the list" )



price = [100,200,300,400,500]
color = ["Red","Blue","Yellow"]
device = ["Tv ","laptop"," printer "]
for prices in price:
    for colors in color:
        for devices in device:
         print(f'{prices} , {colors} , {devices}')