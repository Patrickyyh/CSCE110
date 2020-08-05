# Modifying a list with the  loo

## 1.1 using the copy of the list while using the for loop :

 

```python
num1 = [5,10,15]
num2 = [10,15]
for val in nums1[:]:
    if val in num2:
        num1.remove(val)
```

## 1.2 Using sorted() built in function to sort the list

```python
# if use  sort() function:
# this funtion will put the low_case letter at the back of 
# the list
# Method: to deal with it 
# sorted have an key argument.The key specifies a function 
# to be applied to each element prior to being compared 

sorted(num1,key = str.lower)

my_list = [[25], [15, 25, 35], [10, 15]]

sorted_list = sorted(my_list, key=max)
print('Sorted list:', sorted_list)








```



# Lecture 15 (set)

## 1.1Properties of set

1. mutable and unordered

2. add method adds a single element

3. The update() method adds multiple elements (tuples, lists, strings, sets)

4. since the set is mutable ,so you cannot have an mutable objects

   in the set (like the list  in the set )



**Elements of sets are immutable. Elements of sets are unique. Sets cannot be indexed.**



The Set cannot be indexed

The elements can be heterogeneous: integer, float, tuple, string







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

### 2.11 Keys:

1. are immutable
2. can be strings, numbers and tuples
3. are unique in the dictionary

### 2.22 values:

1.are mutable

2.can be any data type

3.can appear repeatedly in the dictionary



###  2.23 Dictionary methods:

Methods: keys() values() items()  return list_like values of a dictionary's keys

```python
#The dict type also supports the useful methods items(), keys(), and values() methods, which produce a view object. A view object provides read-only access to dictionary keys and values. A program can iterate over a view object to access one key-value pair, one key, or one value at a time, depending on the method used. A view object reflects any updates made to a dictionary, even if the dictionary is altered after the view object is created.
```

values, or both keys and values 

1. The values returned are not true lists.

2. The values cannot be modified and do not have an append() method.

3. The values returned are iterable and can be used in for loops.

4. delete an item from the dic :  del  dict["something"]

5. remove an arbitrary item from the dictionary:

      item = scientist.popitem()

   6. remove all items from the dictionary:

      scientists.clear()

   7. 

   

   

   ### Accessing elements  from the elements:

   use method get()

   

   ### Sorted method  : 

   The sorted method returns a sorted list of keys in the dictionary.

   

   <img src="C:\Users\e3270\Desktop\dictionary_method.png" style="zoom:70%;" />

   

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
   # you also could modified the the second parameter
   # in the get method, if the key was not 
   # in the dictionary, the result will be given out 
   
   student.get("gg","sory cannot find this key")
   >>>'sory cannot find this key'
   
   #change the value in the dictionary
   book[2018] = ["The first one","Elvaton"]
   
   # using the comprehension to create a new dicitonary from iterable
                # key  value
   even_numbers ={n : (2 * n) for n in range(5)}
   print(even_numbers)
   #                                            we can also write a conditional                                                   statement over here
   even_numbers = {n: n for n in range(0,10) if n % 2 == 0}
   
   # check the membership of the key in the dictionary
   2001 in book
   >>False
   reason: the key 2001 was not in this dictionary
       
   
   ```

### 2.24 The ways to  sort dictionary;

### Sorted method  : 

**The sorted method returns a sorted list of keys in the dictionary.**

#### 1.ordered by values;



Sorted by descending  order:   sorted(student.values(),reverse = True)
['2000', '1220', '1200', '0032']

#### 2 ordered

#### 3. ordered  by  items:



```python

# This Little program order the element in the dictionary
# by ascendding order in birth .
student = {'tom': '1220', 'pat': '1200', 'got': '2000', 'tog': '0032'}
ordered_student = dict()
sorted_value = sorted(student.value())
for student_birth in sorted_value:
    ordered_stuent[student_birth] = student.get(student_birth)
    
print(ordered_student)


#swap keys and values:
reversed_student = dict();
#iterate it by items
for student_name, students_birth in students.items():
    reversed_student[students_birth] = student_name



## simpler way to do it 
sorted_student = dict()

#Ascending order
for year in sorted(student.value(),reverse = False):
    ordered_student[year] = student.get(year)
    
 # Descending order   
for year in sorted(student.value(),reverse = True):
    ordered_student[year] = student.get(year)
    
    
   
```





# Lecture 17   Tuples

## 1.1 Property of the the Tuples;

1. a sequence of value:

2. can be any type

3. indexed by integers

4. not immutable

   much more like a string 

   

   ```python
   t= ('a','b','c','d')
   ```

   

## 1.2 Creating a tuples

 A value in parentheses is not a tuple 

```python
t2 = ("a") # t2 is not a tuple. t2 is a string 
t1 = ('a',)# t1 is a tuple
# creating tuple constructor
t = tuple()
#If the argument is a sequence , the result is a tuple
#with the elements of the sequence
t = tuple('python')
>>>t
('p','y','t','h','o','n')


```





## 1.3 Indexing

Like a strings, each element in a tuple has an index, The index operator[ ] accesses an element in the tuple.



##  1.4 Slicing

Exactly the same as previous sequence



## 1.5  Swap two variables

###  1. conventional way - using a temporary variable



## 1.6  delete del

1. Since a tuple is immutable, we cannot change or delete the items in a tuple 

   The del keyword deletes the entire tuple,

## 1.7 count() and index()

```python
tuple.count(x) # counts the number of times the item x appears
tuple.index(x) # returns the 1st index where the item x is found

```







