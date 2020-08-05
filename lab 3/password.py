pass_list= input("Enter a password: ")
while(True):

  if len(pass_list)>=4 and len(pass_list)<=8:
     if (pass_list[0].isupper()) and (pass_list[len(pass_list)-1].isnumeric()):
         print(f"{pass_list} is valid!")
         break
     else:
         pass_list = input(f"{pass_list} is invalid, try again: ")
  else:
     pass_list = input(f"{pass_list} is invalid, try again: ")




