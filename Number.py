
def divisors(n):
    return cast(n)[0]
def primes(n):
    cast(n)[1]
def relPrimes(n):
    primes = []
    for i in range(2, n+1):
        if commonDiv(i, n) == [1]:
            primes.append(i)
    return primes
def commonDiv(a, b):
    divs = []
    primes = []
    for k in divisors(a):
        if k in divisors(b):
            divs.append(k)
    return divs
def cast(n):
    divisors = []
    primes = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
            burn = 0
            for j in range(2, i):
                if commonDiv(i, j) == [1]:
                    continue
                else:
                    burn+=1 
            if burn == 2:
                primes.append(i)
    return divisors, primes