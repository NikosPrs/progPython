
def primes(n):
    primes=[]
    for i in range(2, n):
        divs=[]
        for j in range(2, i):
            if i % j == 0:
                divs.append(j)
        if divs == []:
            primes.append(i)
    return primes
def quantity(n):
    quantity = []
    for i in primes(n):
        if n%i == 0:
            k = 1
            while n%(i**k) == 0:
                k = k + 1
            quantity.append(k-1)
        else:
            continue
    return quantity
def primesIn(n):
    rel = []
    for i in primes(n):
        if n%i == 0:
            rel.append(i)
    return rel
