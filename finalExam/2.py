'''


Write a function that checks whether a given string is a pangram or not.
A pangram is a sentence that contains every letter of the alphabet at least once


'''

def check_pagram(setence):
     all_letter = [ chr(ord('a')+n) for n in range(0,26)]
     for n in sentence:
         for letter in range(len(n)):
             if n[letter].lower() not in all_letter:
                 return False

     return True





sentence = input("Please enter the setence: ").split()
print(check_pagram(sentence))