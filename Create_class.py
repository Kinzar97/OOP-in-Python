from random import randint


class Warrior:
    health = 100

    def damage(self):
        h = self.health - 20
        print('У противника осталось:', h, "здоровья", end='\n\n')
        return h


warrior1 = Warrior()
warrior2 = Warrior()

print('Привет, человек!\n\nТы попал в игру "Гладиаторы". В этой игре тебе ничего не нужно делать. Ты будешь лишь смотреть, как сражаются гладиаторы!\n\nПриятного просмотра!',
    end='\n\n\n')
while warrior1.health > 0 and warrior2.health > 0:
    n = randint(1, 2)
    if n == 1:
        print('Гладиатор 2 атаковал!')
        warrior1.health = warrior1.damage()


    else:
        print('Гладиатор 1 атаковал!')
        warrior2.health = warrior2.damage()

if warrior1.health == 0:
    print('Победил Гладиатор 2')
else:
    print('Победил Гладиатор 1')
