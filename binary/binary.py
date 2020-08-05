numbers = [25,16,128]
for n in numbers:
    try:
        print(hex(n))
    except TypeError as  e:
        print(f"Error {e} has occured")


def mask():
   return(bin(0b1100 | 0b1010))








print(int('110',2))
## The base of the result is two ,
number = bin(int('110',2) + int('110',2))
print(number)
print(int(number,2))
print(mask())
