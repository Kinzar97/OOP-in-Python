class Data:
    def __init__(self, *info):
        self.info = list(info)

    def __getitem__(self, i):
        return self.info[i]


class Teacher:
    def teach(self, info, *pupil):
        for i in pupil:
            i.take(info)


class Pupil:
    def __init__(self):
        self.knowledge = []

    def take(self, info):
        self.knowledge.append(info)

    def forget(self):
        from random import randrange
        del self.knowledge[randrange(len(self.knowledge))]

lesson = Data('class', 'object', 'inheritance', 'polymorphism', 'encapsulation')
marIvanna = Teacher()
vasy = Pupil()
pety = Pupil()
marIvanna.teach(lesson[2], vasy, pety)
marIvanna.teach(lesson[0], pety)

print(vasy.knowledge)
print(pety.knowledge)

vasy.take('Composition')
vasy.take('Composition1')
vasy.take('Composition2')
print(vasy.knowledge)

vasy.forget()
print(vasy.knowledge)

vasy.forget()
print(vasy.knowledge)