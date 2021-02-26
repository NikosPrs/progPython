
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
def primeDec(n):
    k=0
    s = ' n = '
    for prime in primesIn(n):
        s += str(prime)+'^'+str(quantity(n)[k])+'*'
        k+=1
    w=s[0:len(list(s))-1]
    return w
def mcd(n, m):
    mcd=1
    k=0
    minQuantity=[]
    index = 0
    for prime1 in primesIn(n):
        index += 1
        index1 = 0
        for prime2 in primesIn(m):
            index1 += 1
            if prime1 == prime2:
                w = primesIn(m).index(prime2)
                minQuantity.append(quantity(n)[w])
                mcd *= prime1**minQuantity[k]
                k+=1
    return mcd


