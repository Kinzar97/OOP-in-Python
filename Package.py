"""Модуль содержит классы обьектов внутри комнаты"""

class Win_Door:
    """Класс Окна и Двери.
Конструктор принимает длину и ширину окна или двери и рассчитывает площадь"""
    def __init__(self, x, y):
        self.square = x * y


class Room:
    """Класс Стены.
Конструктор принимает длину, ширину и высоту стен комнаты"""
    def __init__(self, x=0, y=0, z=0):
        self.width = x
        self.lenght = y
        self.height = z
        self.wd = []

    def Fullsquare(self):
        """Метод для вычисления площади стен внутри комнаты"""
        return 2 * self.height * (self.width + self.lenght)

    def addWD(self, w, h):
        """Метод для добавления онка или двери в список обьектов внутри комнаты"""
        self.wd.append(Win_Door(w, h))

    def workSurface(self):
        """Метод для вычисления площади для обклеивания обоями"""
        new_square = self.Fullsquare()
        for i in self.wd:
            new_square -= i.square
        return new_square

    def count(self, l, w):
        """Метод для вычисления количества рулонов обоев для обклейки комнаты"""
        if self.workSurface() % (l * w) == 0:
            return int(self.workSurface() / (l * w))
        else:
            return int(self.workSurface() / (l * w)) + 1
