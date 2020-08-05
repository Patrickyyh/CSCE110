def nfact(n):
    if n == 1 or n ==0 :
        fact  =1
    else:
        fact = n * nfact(n-1)
    return fact



print(nfact(4))