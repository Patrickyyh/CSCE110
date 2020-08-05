# File: q3.py
# Author: Yuhao Ye
# Date: 06/13/2020
# Section: 529006730(UIN)
# E-mail: yeyuhao1234@tamu.edu
# Description:
#This probram take the loan interest rate
# and period. Then print out the total pay off
#amount

rate = float(input("Enter the interest rate (in percentage): "))
period = float(input("Enter the loan period (int years): "))
print()
Total_Payoff = ( 1 + (rate/100) )**period * 15000
print(f'At {rate}% interest, you will need to pay ${round(Total_Payoff,2)} after {period} years')
