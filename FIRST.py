#x = int(input("Enter the value of the x: "))
#if ( x > 30 ):
#    print('A')
#else:
#    print('B');
#print('C') # the c is uncontional case:
#
#print("The first on of the videos is the second one ")

# the empty string is also bool
# None 0 False all of those belong to 0 boolean type
#hence, we could use boolean to verify if the container or string is empty
# if  100 /21 , the result of this is an float number.
# the logicl operator in the python
# and &&     || or  , not
# Membership operators#
##  in: true if a variable is in the sequence, false otherwise
## not in , true if a variable is not in the specificed sequence, false otherwise
state = input("Please enter the name of the state ; ")
state_lower = state.lower()
letter = input("Please enter the letter: ")
letter_lower = letter.lower()
if letter_lower in state_lower:
    print(f'{letter} is in {state}')
else:
    print('There is no letter in the state name')
# this verison is different from the version made by the professor
# i just polished it and made it nelegect the whether the character is
#lower or upper version


#To test if the the word is symmertrical

number  = input("Enter the number ")
print(f'the number {number} symmetrical? {number == number[::-1]}')



