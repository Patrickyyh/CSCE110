

count = 20
for number in range(12):
    count +=1

#iterator and step
#                range and step
for number in range(1,13,2):
    print(f'{number}')



for name in ['Patrick', 'Tom', 'erin','corina']:
     print(f'check {name}')
     if (len(name)  < 4):
         print(f'{name} you have to check it ')
         break; # the loop break over here