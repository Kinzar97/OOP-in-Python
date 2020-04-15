from random import randint


class Unit():
    def __init__(self, sp_n=0, com=0):
        self.spec_num = sp_n
        self.command = com


class Hero(Unit):
    level = 1

    def up_level(self):
        self.level += 1


class Soldier(Unit):
    def Follow_Hero(self, hero):
        self.command = hero.command


hero1 = Hero(1, 1)
hero2 = Hero(2, 2)
sp1 = []
sp2 = []
i = 0
while i < 11:
    sold = Soldier(i + 2, randint(1, 2))
    if sold.command == 1:
        sp1.append(sold)
    else:
        sp2.append(sold)
    i += 1

if len(sp1) > len(sp2):
    hero1.up_level()
else:
    hero2.up_level()

print(len(sp1), len(sp2))
print('The first hero level:', hero1.level, ';', 'The second hero level:', hero2.level)

sp1[3].Follow_Hero(hero2)

print(hero1.spec_num, sp1[3].spec_num, sp1[3].command)
