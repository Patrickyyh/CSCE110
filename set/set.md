# Lecture 15 (set)

## 1.1Properties of set

1. mutable and unordered

2. add method adds a single element

3. The update() method adds multiple elements (tuples, lists, strings, sets)

4. since the set is mutable ,so you cannot have an mutable objects

   in the set (like the list  in the set )

```python
discard()
method removes an item from a set   


remove()
method removes an item from a set and it raises a error if the item does not exit. 

pop()
remobe and returns an element

clear()
removes all elements from the set.


```



```python
oster = set(list(range(10)))
print(roster)
roster = input("Enter numbers: ").split(sep=',')
##efficient way to conver string in a set to the int number:
roster =[int(n) for n in roster]
# create an empty set
a = set()


roster = {1,3}
roster.add(2)
roster.update{[2,3,4]}
roster.update{[4,5],{1,6,8}}

```

------

## 1.2 Set operation

Set Union 

Sets Intersection:

Sets Difference:

Symmetric Difference:

   The symmetric Difference of A and B is a set of elements 

in both A and B except those that are common in both 



Set Complement 

The complement of A is the set of all element in U but not in A



```python
Unions
majors = {'eng','cs','bio'}
minors = {'ee','bus','hist','pol','cs','eng'}
majors.union(minors)

Sets Intersection:
 majors.intersection(minors)
    
    
majors = {'eng','cs','bio'} minors = {'ee','bus','hist','pol','cs','eng'}
majors.intersection(minors)
{'cs', 'eng'}
majors.difference(minors)
{'bio'}

majors.symmetric_difference(minors)
{'hist', 'pol', 'bus', 'ee', 'bio'}

Union:
    major | minors
Intersection:
    majors & minos
    
minors 

```



# Lecture 16 (dictionary )

## 2.1  Features of Dictionary 

1. unordered collection of elements

2. mapping between the keys and sets of values

   they are mutable

3. Each key maps to a value, the association of a key and 

   a value is called key-value pair

### Keys:

1. are immutable
2. can be strings, numbers and tuples
3. are unique in the dictionary

### values:

1.are mutable

2.can be any data type

3.can appear repeatedly in the dictionary



###  Dictionary methods:

Methods: keys() values() items()  return list_like values of a dictionary's keys

values, or both keys and values 

1. The values returned are not true lists.

2. The values cannot be modified and do not have an append() method.

3. The values returned are iterable and can be used in for loops.

   

   

   ### Accessing elements  from the elements:

   use method get()

   

   

   ```python
   
   book = {2018:['Educated','becoming','the outsider'], 2019:['The silent patient','the testmate']}
   book.keys()
   dict_keys([2018, 2019])
   #/////
   book.values()
   dict_values([['Educated', 'becoming', 'the outsider'], ['The silent patient', 'the testmate']])
   
   book.items()
   dict_items([(2018, ['Educated', 'becoming', 'the outsider']), (2019, ['The silent patient', 'the testmate'])])
   
   ## use for loop to iterate the key, values in the dictionary
   book = {2018:['Educated','becoming','the outsider'], 2019:['The silent patient','the testmate']}
   for years in book.keys():
       print(f'{years}')
   for books in book.values():
       print(f'{books}')
   for years,books in book.items():
       print(f'Published in {years}: {book}')
   #:The result of the code above    
   2018
   2019
   ['Educated', 'becoming', 'the outsider']
   ['The silent patient', 'the testmate']
   Published in 2018: {2018: ['Educated', 'becoming', 'the outsider'], 2019: ['The silent patient', 'the testmate']}
   Published in 2019: {2018: ['Educated', 'becoming', 'the outsider'], 2019: ['The silent patient', 'the testmate']}
       
       
       
   ## Accessing elements from the dictionary
   print(book.get(2019))
   book[2019]
   
   #change the value in the dictionary
   book[2018] = ["The first one","Elvaton"]
   
   # using the comprehension to create a new dicitonary from iterable
                # key  value
   even_numbers ={n : (2 * n) for n in range(5)}
   print(even_numbers)
   #                                            we can also write a conditional                                                   statement over here
   even_numbers = {n: n for n in range(0,10) if n % 2 == 0}
   
   
   ```





## 2.2 









