my_list = []
for num in range(10):
    my_list.append(num)


my_seocndList = list(my_list)
for ele in my_seocndList:
    print(ele,end = ' ' )


print()
if bool(my_seocndList) and bool(my_list):
    print("Both of them have the elements")
else:
    print("one of the them does nothave the value")


## List compehension
## dynamically add the element in the list
odd_numbers = [2 *n+1 for n in range(10)]
print(odd_numbers)
print()

even_number = [n for n in range(20) if n % 2 == 0]
print(even_number)
print()

even_number =[n for n in range(2,12) if n % 2 ==0]
print(even_number)



even_number = even_number + odd_numbers
print(even_number)
print(len(even_number))
even_number.pop()
print(even_number)

countries = ["japan" , "Thailand " , "China"]
countries2 = ["Usa" , "German"]
countries2.extend(countries)
print(countries2[::-1])
print(countries2[::])

total_country = [["japan" , "Thailand " , "China"],["Usa" , "German"] ]
print(total_country)

countries = total_country
print(countries)

## consider it as the reference
## like the pointer in the c++ and Java()
countries[1][0] = 'apple'
print(countries)
print(total_country)

## insert(position , elements)


#remove something
#remove(elements)

#count(elements)
# will return how many does specific items appears in the list

#pop(index)
#will pop up specific elements from the list and return this element

majors = ['math', 'eng', 'biology', 'computer science', 'history', 'business']
print(majors)

majors.sort()
print(majors)
majors.sort(reverse=True) ## print in descending order
print(majors)
copy_major = majors.copy()
print()

## copy() make a copy of list and sent it the a new list
print(copy_major)


##majors.sort()
##If a key function is given, apply it once to each list item and sort them,
##ascending or descending, according to their function values.


## List delet
#was able to delet whole list


