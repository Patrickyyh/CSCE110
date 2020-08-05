# File: q1.py
# Author: Yuhao Ye
# Date: 07/03/2020
# Section: 529006730(UIN)
# E-mail: yeyuhao1234@tamu.edu
# Description:
# Take a text and prints the number of occurrences of eacht letter


line = input("Enter a Sentence: ").split()
print()
print("Sentence Statistics:")
letter_dict = dict()
count = 0
for word in line:

    letter = list(word)
    for letters in letter:
        letters = letters.lower()
        if(letters.isalpha()):
            for key in letter_dict.keys():
                if letters == key:
                      letter_dict[letters] = letter_dict[letters] + 1
                      count +=1
            if count == 0:
               letter_dict[letters] = 1
            count = 0
count = 1

## store the occurencs
times_count = list()
## store the letters in alphabetical order
order_dict2 = dict()


for values in sorted(letter_dict.values(),reverse=True):
    if values not in times_count:
        times_count.append(values)




for key in sorted(letter_dict.keys()):
    order_dict2[key] = letter_dict.get(key)



for number in times_count:
    for key,value  in order_dict2.items():
          if value == number:
              print(f'{key} appeared {value} times.')
    print()






