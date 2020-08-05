# File: q1.py
# Author: Yuhao Ye
# Date: 07/18/2020
# Section: 529006730
# E-mail: yeyuhao1234@tamu.edu
# Description:
#  Generates several file to show the frequency of occurrence of word.




##
each_word= list()             # Store the words in text
words_count = dict()          # Store the frequency of occurrence : key : word , value : amount
invert_wordsCount  = dict()   # Store the frequency of occurrence : key : amount  , value : word
even_word = 0                 # Store the amount of even frequency of occurrence
odd_word = 0                  # Store the amount of odd frequency of occurrence


## FileInputStream
## read the words in txt into the each_word
with open('q1_text.txt','r')as read:
     count = 0
     words =  read.read()
     each_word = words.split()


for word in each_word:
    word = word.lower()
    if word not in words_count:
       words_count[word] = 1
    else:
       words_count[word] +=1


# invert_wordsCount store the occurence
for word,value  in words_count.items():
    invert_wordsCount[value] = invert_wordsCount.get(value,[])  + [word]


## create odd_words.txt
with open('odd_words.txt', 'w') as write:
    write.write("The words occurring an odd numbers of times are: \n")
    for key ,word in sorted(invert_wordsCount.items(),reverse= True):
      if (key % 2 != 0 ):
        for x in range(len(word)):
           write.write(f'{word[x].capitalize()} - {key}\n')
           odd_word += 1
## create even_word.txt
with open('even_words.txt','w')as write:
    write.write("The words occurring an even numbers of times are: \n")
    for key , word in sorted(invert_wordsCount.items(), reverse= True):
        if(key % 2 == 0):
            for x in range(len(word)):
               write.write(f'{word[x].capitalize()} - {key}\n')
               even_word +=1


## Create the details.txt
with open('details.txt','w') as write:
    count =0
    write.write('The five most frequent words are:\n')
    for key in sorted(invert_wordsCount,reverse = True)[:5:]:
         for word in invert_wordsCount[key]:
             count += 1
             write.write(f'{word.capitalize()} - {key}\n')
             if count >=5:
                 break
    write.write('\n')
    write.write(f'The total number of words occurring an odd number of times: {odd_word}\n\n')
    write.write(f'The total number of words occurring an even number of times: {even_word}\n\n')
    write.write(f'The total number of words: {odd_word  + even_word }\n\n')




