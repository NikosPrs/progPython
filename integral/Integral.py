import math
class Integral:
    def __init__(self, n, L):
        self.point = n
        self.interval = L
    def f(self, x):
        return 2*x
    def step(self, i):
        n = self.point
        L = self.interval
        return (L[1]-L[0])*i/n
    def points(self):
        first = []
        last = []
        n = self.point
        for i in range(n):
            first.append(self.step(i))
            last.append(self.step(i+1))
        return [first, last]
    def imagef(self):
        L = []
        U = []
        n = self.point
        index = self.points()
        for i in range(n):
            for j in range(2):
                if j < 1:
                    x = index[j][i]
                    L.append(self.f(x))
                else:
                    y = index[j][i]
                    U.append(self.f(y))
        return [L, U]
    def createSumList(self):
        low = 0
        up = 0
        img = self.imagef()
        l = img[0]
        s = img[1]
        n = self.point
        for i in range(n):
            low += (1/n)*l[i]
            up += (1/n)*s[i]
        return [low, up]
    def __str__(self):
        return str(self.createSumList())