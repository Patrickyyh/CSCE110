# File: q1.py
# Author: Yuhao Ye
# Date: 06/19/2020
# Section: 529006730
# E-mail: yeyuhao1234@tamu.edu
# Description:
#  calculates what day of the week a certain date will be in a given month.
Day = input("Enter the first day of the month: ")
date = int (input("Enter a date: "))
my_list = ["Monday","Tuesday","Wednesday", "Thursday", "Friday", "Saturday","Sunday"]
suffix = 'th'
print()
if date > 7 :
 date_left= date % 7
else:
    date_left = date
count = 0;
if Day[0] == "M":
    Day = "Monday"
    count  =1
elif Day[0] == "T":
    if Day[1] =="u":
       Day = "Tuesday"
       count = 2
    else:
        Day = "Thursday"
        count = 4
elif Day[0] == "W":
    Day = "Wednesday"
    count =3
elif Day[0] == "R":
    Day = "Thursday"
    count  = 4
elif Day[0] == "F":
    Day = "Friday"
    count = 5
elif Day[0] == "S":
    Day = "Saturday"
    count = 6
elif Day[0] == "U":
    Day = "Sunday"
    count  = 7



if(date_left != 0):
 count = count + date_left-1

 if(count > 7):
     count = count - 7
else:
    count = count + 7 - 1
    if(count > 7):
      count = count -7



for day in my_list:
    if count == (my_list.index(day)+1):
        if (date % 10 == 1):
            suffix = 'st'
        elif (date % 10 ==2):
            suffix = "nd"
        elif (date % 10 == 3):
            suffix = "rd"
        print(f'The {date}{suffix} is a {day}.')








