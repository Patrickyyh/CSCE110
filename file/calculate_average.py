import os
print('Reading in the Data')
path = os.path.join('C:\\','Users','e3270','Desktop','CSCE110','file','mydata.txt')

## get current work directory
current_path = os.getcwd()
path_list = current_path.split(os.path.sep)
print(path_list)

## seperate the path into the tuple
current_path = os.getcwd()
print(os.path.split(current_path))



print(path)
file = open(path)
# we could consider the lines as array over here
#hence we could use for loop to iterate it
lines = file.readlines()
file.close()

total = 0
for line in lines:
    total += int(line)
avg = total/ len(lines)
print(f'The Average number is {avg}')
