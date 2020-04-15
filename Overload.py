class Snow:
    def __init__(self, count):
        self.c = round(count)

    def __add__(self, n):
        self.c += n

    def __sub__(self, n):
        self.c -= n

    def __mul__(self, n):
        self.c *= n

    def __truediv__(self, n):
        self.c /= n
        round(self.c)

    def __call__(self, newcount):
        self.c = newcount

    def makeSnow(self, countrow):
        return int(self.c / countrow) * (countrow * '*' + "\n") + round((self.c/countrow - int(self.c/countrow))*countrow)*'*'

a = Snow(101)
print(a.makeSnow(20))
a + 5
print(a.makeSnow(20))
a / 3
print(a.makeSnow(20))
a - 10
print(a.makeSnow(20))
a * 3
print(a.makeSnow(20))
a(16)
print(a.makeSnow(20))

a(20)
print(a.makeSnow(20))
a(20)
print(a.makeSnow(20))