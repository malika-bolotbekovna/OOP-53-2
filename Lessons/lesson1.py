counter = 0

class Hero:
    

    def __init__(self, name = None, lvl = 1, hp = 100):
        global counter
        if name is None:
            self.name = 'user' + str(counter)
            counter += 1
        else:
            self.name = name

        self.lvl = lvl
        self.hp = hp


    def introduce(self):
        print(f'Привет, меня зовут {self.name}, мой уровень {self.lvl}, мой hp {self.hp}')


    def is_adult(self):
        return self.lvl >= 10


kirito = Hero(lvl = 90, name = 'Kirito', hp = 1000)
kirito.introduce()
print(kirito.is_adult())


mani = Hero(lvl = 9, name = 'Mani', hp = 1000)
mani.introduce()
print(mani.is_adult())


user = Hero( hp = 400)
user.introduce()
print(user.is_adult())

john = Hero(lvl = 123)
john.introduce()
print(john.is_adult())