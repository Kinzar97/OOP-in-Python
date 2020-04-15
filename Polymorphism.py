class Overload():

    def __add__(self, obj2):
        return Overload()
    def __str__(self):
        return "It'is a new object"



a = Overload()
b = Overload()
print(b+a)
