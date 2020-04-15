class Win_Door:
    def __init__(self, x, y):
        self.square = x * y


class Room:
    def __init__(self, x=0, y=0, z=0):
        self.width = x
        self.lenght = y
        self.height = z
        self.wd = []

    def Fullsquare(self):
        return 2 * self.height * (self.width + self.lenght)

    def addWD(self, w, h):
        self.wd.append(Win_Door(w, h))

    def workSurface(self):
        new_square = self.Fullsquare()
        for i in self.wd:
            new_square -= i.square
        return new_square

    def count(self, l, w):
        if self.workSurface() % (l * w) == 0:
            return int(self.workSurface() / (l * w))
        else:
            return int(self.workSurface() / (l * w)) + 1


r1 = Room()

r1.width = float(input('Enter the width of the room (meters): '))
r1.lenght = float(input('Enter the lenght of the room (meters): '))
r1.height = float(input('Enter the height of the room (meters): '))
n = int(input('Enter the number of windows and doors in the room: '))
for i in range(1, n + 1):
    r1.addWD(float(input('Enter the width of the ' + str(i) + ' object (meters): ')),
             float(input('Enter the lenght of the ' + str(i) + ' object (meters): ')))
print('\nThe work surface: {0:.2f} meters.'.format(r1.workSurface()))
print('You need {} rolls of wallpaper 5 X 1.2 meters.'.format(r1.count(5, 1.2)))
