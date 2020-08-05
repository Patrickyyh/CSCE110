# File: q1.py
# Author: yuhao ye
# Date: 07/10/2020
# Section: 529006730
# E-mail: yeyuhao1234@tamu.edu
# Description:
# check the validity of a password chosen by a user
#contain at least 1 letter between [A-Z],
#b) contain at least 1 letter between [a-z],
#c) contain at least 1 number between [0-9],
#d) contain at least 1 special character from [$#@],
#e) have a minimum length of 6 characters, and
#f) have a maximum length of 12 characters.




def validate(line):
   special_character = ['$', '#', '@']
   condition = list()
   low_letter= [ ]
   if len(line) >= 6 and len(line) <=12:
      for letter in line:
          if letter in special_character:
              condition.append(1)
          elif ord(letter) in range(65,91):
              condition.append(2)
          elif ord(letter) in range(97,123):
              condition.append(3)
          elif ord(letter) in range (48,58):
               condition.append(4)

      condition_uniqu = set(condition)

      for num in range(1,5):
          if num not in condition_uniqu:
              print('not valid')
              return False
      print('valid')
      return True
   else:
       print('not valid')
       return False


def main():
  special_character = ['$','#','@']
  valid_pwd = list()
  invalid_pwd = list()
  while(True):
    line = input('> ').strip()
    if line =='quit':
        print(f'> {len(valid_pwd)} valid passwords:',end = " ")
        print(', '.join(valid_pwd))
        print(f'> {len(invalid_pwd)} invalid passwords:',end = " ")
        print(', '.join(invalid_pwd))
        break
    elif line in valid_pwd:
        print('already validated')
        continue
    else:
       validate_result = validate(line)
       if validate_result == True:
           valid_pwd.append(line)
       else:
           if line not in invalid_pwd:
              invalid_pwd.append(line)

if __name__ == '__main__':
    main()
