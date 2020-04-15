class HideMan:
    def __init__(self, name=None, sname=None, age=None):
        self.__name = name
        self.__surname = sname
        self.__age = age

    def getInfo(self):
        return self.__name + self.__surname + str(self.__age)

    def setInfo(self, name, sname, age):
        self.__name = self.__setUp(name)
        self.__surname = self.__setUp(sname)
        self.__age = self.__setUp(age)

    def __setUp(self, up):
        return str(up).upper()

    def __str__(self):
        return 'Test'


n = HideMan('Pet', 'Zam', 23)
print(n.getInfo())

n.setInfo('Igor', 'Zaripov', 21)
print(n.getInfo())

print(n)
