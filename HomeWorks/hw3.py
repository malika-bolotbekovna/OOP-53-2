from main import Hero

class Jester(Hero):
    def __init__(self, name = None, hp = 100, magical_attacks = None):
        super().__init__(name, hp, magical_attacks)

    def unique_attack(self):
        print('\nillusion of lie')

    def unique_scream(self):
        print(f'\nstun of {self.name}')

    def action(self):
        answer = super().get_random_int()
        if answer == 1:
            print(f'\nrandom integer number: {answer}')
            super().attack()
            print('method attack is called from the class Hero')

        elif answer == 2:
            print(f'\nrandom integer number: {answer}')
            super().protection()
            print('method protection is called from the class Hero')

        else:
            print(f'\nrandom integer number: {answer}')
            super().rest()
            print('method rest is called from the class Hero')


mani = Jester(hp = 888)
mani.unique_attack()
mani.unique_scream()
mani.action()
