happy_number = list()
prime_number = list()
overlap = list()
with open("happynumbers.txt","r") as read:
    number = read.readline().strip()
    while(number!=""):
        happy_number.append(number)
        number  = read.readline().strip()



with open("primenumbers.txt","r") as read:
    number = read.readline().strip()
    while(number!=""):
        prime_number.append(number)
        number  = read.readline().strip()

for number in happy_number:
    if number in prime_number:
        overlap.append(number)


print(overlap)