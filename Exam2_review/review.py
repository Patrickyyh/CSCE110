a = "1,2,3"
print(a.split(","))
b = "     hi there! "
print(b.strip())
d =" 45 15 150 1955"
print(d.split("5"))

# Write a Python program that prompts the user for number n
# and calculates the factorial of that number n
def factorial(n):
    list= [n for n in range(1, n+1)]
    total = 1
    for number in list:
        total  = total *number
    return total


def histogram(list):
    for number in list:
        for i in range(int(number)):
            print('*', end="")
        print()




#
times = [ " 2:09 " , { " 8:23 " , " 3:32 "} , {" 2:52 " , " 12:44 " , " 12:02 " }]
print(times)
for day in times:
    print("day:" , day)
    for times in day:
        print("time:" , times)
    print()


fruits = ["cheery","strawberry rhubarb","app"
                                        "le"]
fruits_pie= [fruit + " pie" for fruit in fruits]
print(fruits_pie)
print([fruit.count("r") for fruit in fruits])

vec1 = [2,4,6]
vec2 = [4,3,-9]
#Notice the difference between these two statement

print([x*y for x in vec1 for y in vec2])
print([vec1[i] * vec2[i] for i in range(len(vec1))])

line = input('Enter a string of positive integers sepatated by spaces: ').split()
histogram(line)