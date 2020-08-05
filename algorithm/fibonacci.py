def fibo(n):
    if n == 0 or n ==1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def power(a,n):
    if n == 1:
       return a
    else:
       a * power(a,n-1)


print(factorial(5))