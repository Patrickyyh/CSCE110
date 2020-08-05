file_1 =input('Enter the name of file 1: ')
file_2 = input('Enter the name of file 2: ')
store_1 = list()
store_2 = list()
try:
  with open(file_1,'r') as read:
      store_1 = read.readlines()

  with open(file_2,'r')as read:
      store_2 = read.readlines()

except FileNotFoundError as e:
    print(e)
try:
  with open(file_2,'w')as write:
      for line in store_1:
          write.write(line)
except FileNotFoundError as e:
  with open(file_1,'w')as write:
      for line in store_2:
         write.write(line)