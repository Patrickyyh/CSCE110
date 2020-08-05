# File: q6.py
# Author: Yuhao Ye
# Date: 06/13/2020
# Section: 529006730(UIN)
# E-mail: yeyuhao1234@tamu.edu
# Description:
# take a setence without any punctuation
# print the number of letters and the nunber of vowels in
# the sentence


setence = input("Enter text: ")
print()
letter_count = 0
vowels_count = 0
for letter in setence:
    if (letter!=" "):
        letter_count +=1
        if letter.lower() == 'a' or letter.lower() == 'e' or letter.lower() == 'i' or letter.lower() == 'u' or letter.lower() == 'o':
            vowels_count +=1

print(f'This sentence has {letter_count} letters. {vowels_count} of them are vowels.')