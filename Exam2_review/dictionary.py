stop = int(input("Enter the stop number : "))
stor = dict()
for number in range(1,stop+1):
    stor[number] = number * number
print(stor)


sample_data = {"1":["a","b"] , "2":["c","d"]}


list_key = list()
list_key = [n for n in sample_data.keys()]
list_result = list()
print(list_key)
for n in range(len(list_key)-1):
    print(n)
    for x in range(n+1, len(list_key)):
          for values  in sample_data[list_key[n]]:
              for values_second in sample_data[list_key[x]]:
                     result = values+values_second
                     list_result.append(result)



print(list_result)



