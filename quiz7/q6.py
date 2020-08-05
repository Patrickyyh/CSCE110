line = input('Enter a sentence: ').split()
with open('book.txt','w')as my_book:
    for words in line[::-1]:
        words = f'{words}\n'
        my_book.write(words.upper())

