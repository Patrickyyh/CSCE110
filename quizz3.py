word = input("Enter a word:")
length   = len(word)
if length == 0 :
    print("Result: empty!")
elif  1<= length <=4 :
    print(f'Result: {word[::-1]}')
else :
      word1 = word[0:2]
      word2 = word[length - 2 : length]
      word3 = word1 + word2
      print(f'Result: {word3}')