n=20
def Primes(n):
    Primes=[]
    for i in range(2,n):
        divs=[]
        for j in range(2,i):
            if i % j == 0:
                divs.append(j)
        if divs == []:
            Primes.append(i)
    return Primes           
print(Primes(n))
