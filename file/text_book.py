import sys

try:
    with open("textbook.txt","x")as f:
        distance = {'earth':0 , 'Mars':100 , 'Jupter':30 }
        for object , distances in distance.items():
            line = f'The distance from earth to {object} is {distances}\n'
            f.write(line)
    with open('textbook.txt','r')as my_book:
        line = my_book.readline()
        print(line,end='')
        while line !="":
            line = my_book.readline()
            print(line,end = '')
    #replace readline with readlines()
    with open('textbook.txt','r')as my_book:
        line_list = my_book.readlines()
        for line in line_list:
            print(line,end='')


except FileExistsError:
    print(f'The file already exists, please creat a new file. ')
    file_name = input("Enter a new File name")
    with open(file_name,'x')as f:
        f.write('Favorite cities')