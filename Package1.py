from Package import *

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



