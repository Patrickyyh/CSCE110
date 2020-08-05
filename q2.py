# File: q2.py
# Author: Yuhao Ye
# Date: 06/13/2020
# Section: 529006730(UIN)
# E-mail: yeyuhao1234@tamu.edu
# Description:
# This program take the number of visitors today and yesterdau
# and prints the percentange change in website and the difference
#  between two days
YesTerDay = int(input("Enter yesterday's vistor count: "))
ToDay = int(input("Enter today's vistor count: "))
print()
if (ToDay < YesTerDay):
    differnce = YesTerDay- ToDay
    change =  100 * (differnce / YesTerDay)
    print(f"Today's traffic was lower by {differnce} people")
    print(f"The website's traffic change is {round(-change)}%.")



elif (ToDay > YesTerDay):
    differnce = -(YesTerDay - ToDay)
    change = 100 * (differnce / YesTerDay)
    print(f"Today's traffic was higher by {differnce} people")
    print(f"The website's traffic change is {round(change)}%.")
else:
    print(f'The traffic today was unchanged.')
