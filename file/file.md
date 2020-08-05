# File IO Text

## Description

A text file only contains text and no special formatting 

such as bold text, italic text , images



Lines are broke up with special characters. 

`open`: creates a file object 

> The file object is also called a handle, it is used to read or write to the file
>
> `Filename` is the path the file
>
> `mode` is the file system permission

![image-20200708030249040](C:\Users\e3270\AppData\Roaming\Typora\typora-user-images\image-20200708030249040.png)

```python
import os
## use os library to get work direction 
os.getcwd()

```

`r+`: write and read at the same time

Remember to close the file : save the resource .

Notice: The difference between Java Io file and python File

In java you could use flush to flush the byte in the buffer to the destination file.

In python, when you close the file, The information will be flushed into the destination. automatically, 



```python
import os
try:
    file = open("new_computer.py","x")
finally:
    file.close()
```

If an exception occurs, the code exits without closing the file.

Otherwise, the resource will be waste, and the information could not 

be flushed onto the destination.



> content is buffer, will show you all the invisible special character
>
> print() will translate all the invisible character.
>
> just display differently
>
> 

The open() built-in function requires a single argument that specifies the path to the file. Ex: `open('myfile.txt')` opens myfile.txt located in the same directory as the executing script. Full path names can also be specified, as in `open('C:\\Users\\BWayne\\tax_return.txt')`.



## readline()

`read()`method returns the files contents as a string

> **`file.readlines()`** method returns a list of strings, where the first element is the contents of the first line, the second element is the contents of the second line, and so on. Both methods can be given an optional argument that specifies the number of bytes to read from the file. 

Returns the next line of the file, returning the text up to and including the next newline character. 

> The difference between readline() and readlines()
>
> `readline()`-> read the text  line by line and return the line.
>
> `readlines()`->read all the text into the lines and store them into the list

```python
with open('textbook.txt','r')as my_book:
    line = my_book.readline()
    print(line,end='')
    while line !="":
        line = my_book.readline()
        print(line,end = '')
```

```python
 with open('textbook.txt','r')as my_book:
        line_list = my_book.readlines()
        for line in line_list:
            print(line,end='')


```













- Read mode 'r' opens a file for reading. If the file is missing, then an error will occur.
- Write mode 'w' opens a file for writing. If the file is missing, then a new file is created. Contents of any existing file are overwritten.
- Append mode 'a' opens a file for writing. If the file is missing, then a new file is created. Writes to the file are appended to the end of an existing file's contents.

 Output to a file is buffered by the interpreter before being written to the computer's hard disk. By default, **data is line-buffered, e.g., data is written to disk only when a newline character is output.** Thus, there may be a delay between a call of write() and that data actually being written to the disk. The following illustrates:



A programmer can toggle buffering on/off or specify a buffer size with the optional *buffering* argument to the open() function.



## Interact with the operating system

 The Python standard library's **os module** provides an interface to operating system function calls and is thus a critical piece of a Python programmer's toolbox.

A common error is to reduce a program's portability by hardcoding file paths as string literals with operating system specific path separators. To help reduce such errors, good practice is to use the os.path module,



```python
path = os.path.join('C:\\','Users','e3270','Desktop','CSCE110','file','mydata.txt')
```

```python
current_path = os.getcwd()
path_list = current_path.split(os.path.sep)
print(path_list)
```

> `os.path.split(path)` – *Splits a path into a 2-tuple (head, tail), where tail is the last token in the path string and head is everything else.*
>
> ```python
> ## seperate the path into the tuple
> current_path = os.getcwd()
> print(os.path.split(current_path))
> ```
>
> ![image-20200708185231725](C:\Users\e3270\AppData\Roaming\Typora\typora-user-images\image-20200708185231725.png)



> `os.path.exists(path)` – *Returns True if path exists, else returns False*



> `os.path.isfile(path)` – *Returns True if path is an existing file, and false otherwise (e.g., path is a directory).*



> `os.path.getsize(path)` – *Returns the size in bytes of path.*





The **os.walk()** function 'walks' a directory tree like the one above, visiting each subdirectory in the specified path. The following example walks a user-specified year of the above directory tree.





> > A **with statement** can be used to open a file, execute a block of statements, and automatically close the file when complete.







## The with statement 



> The with statement creates a **context manager**, which manages the usage of a resource, like a file, by performing setup and teardown operations.
>
> > `with` **statement**

```python
print('Opening myfile.txt')

# Open a file for reading and appending
with open('myfile.txt', 'r+') as f:
    # Read in two integers
    num1 = int(f.readline())
    num2 = int(f.readline())

    product = num1 * num2

    # Write back result on own line
    f.write('\n')
    f.write(str(product))

# No need to call f.close() - f closed automatically 
print('Closed myfile.txt')
```



## File exists error

```python
try:
    with open ('travels.txt','x')as f:
        f.write('Favorite cities')
excepte FileExistsError:
    print('File already exists.')
```



```python
import sys
try:
    with open("textbook.py","x")as f:
        f.write('Favorite cities')
except FileExistsError:
    print(f'The file already exists, please creat a new file. ')
    file_name = input("Enter a new File name")
    with open(file_name,'x')as f:
        f.write('Favorite cities')
    
```



```python
import sys
try:
    with open("textbook.txt","x")as f:
        distance = {'earth':0 , 'Mars':100 , 'Jupter':30 }
        for object , distances in distance.items():
            ## creat an line, then write it up 
            line = f'The distance from earth to {object} is {distances}\n'
            f.write(line)
except FileExistsError:
    print(f'The file already exists, please creat a new file. ')
    file_name = input("Enter a new File name")
    with open(file_name,'x')as f:
        f.write('Favorite cities')
```