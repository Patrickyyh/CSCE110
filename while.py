user_input = input()
hourly_temperature = user_input.split()

''' Your solution goes here '''



for temp in hourly_temperature:
    print('{}'.format(temp),end = ' ')
    if(hourly_temperature.index(temp) != (len(hourly_temperature) -1) ):
        print('->',end=" ")
        continue;
    print()








