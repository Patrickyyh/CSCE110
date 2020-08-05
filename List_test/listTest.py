major = ["math", "science", "google",'baidu','math','computer']
count_number = major.count("math")
count = 0
temp_index = 0
firts_index = 0
index_list = []

while(True):
    firts_index = major.index("math",temp_index)
    print(firts_index)
    index_list.append(firts_index)
    temp_index = firts_index + 1
    count +=1
    if(count == count_number):
        break



for  number in index_list:
    print("The postion of math inthe list is {}".format(number))


del major
