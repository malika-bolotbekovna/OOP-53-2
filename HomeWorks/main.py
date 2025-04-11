from abc import abstractmethod, ABC

counter = 0
import time
import random


class Hero(ABC):

    def __init__(self, name = None, hp = 100, magical_attacks = None):
        global counter
        if name is None:
            self.name = 'user' + str(counter)
            counter += 1
        else:
            self.name = name

        self.__random_int = random.randint(1, 3)
        self.hp = hp
        self.magical_attacks = magical_attacks

    def protection(self):
        print(f"{self.name} is protected.\n")

    def attack(self):
        attacks=['basic attack', 'charged attack','magical attack', 'poisonous attack', 'life-stealing attack']
        print(attacks)
        choice = input("choose an attack:")
        if choice == attacks[0]:
            print('the opponent is kicked!\n')
        elif choice == attacks[1]:
            print('the attack is charging up...')
            time.sleep(3)
            print('the opponent is punched!\n')
        elif choice == attacks[2]:
            if self.magical_attacks is None:
                print('you have no magic!\n')
            else:
                magics = [magic for magic in self.magical_attacks if magic is not None]
                print(f'your magical attacks: {magics}\n')
                choice = input('choose your magical attack: ')
                if choice == 'water' and 'water' in self.magical_attacks:
                    print('tsunami wave\n')
                elif choice == 'stone' and 'stone' in self.magical_attacks:
                    print('stone spikes\n')
                elif choice == 'fire' and 'fire' in self.magical_attacks:
                    print('fireball\n')
                elif choice == 'air' and 'air' in self.magical_attacks:
                    print('wind barrier\n')
                else:
                    print("you don't have that kind of magic!\n")
        elif choice == attacks[3]:
            print('the opponent was poisoned\n')
        elif choice == attacks[4]:
            print('200hp is stolen\n')
            self.hp += 200
        else:
            print("you don't have that kind of attack!\n")

    def rest(self):
        seconds = (1000 - self.hp) // 100
        if (1000 - self.hp) % 100 != 0:
            seconds += 1
        print(f'healing started for {seconds} seconds. Waiting...')

        while seconds > 0 and self.hp < 1000:
            time.sleep(1)
            seconds = max(0, seconds - 1)
            self.hp += 100
            if self.hp > 1000:
                self.hp = 1000
            print(f'\rtime remaining: {seconds} seconds, hp: {self.hp}', end='',flush=True)

        print('\nhealing is finished.\n')

    def get_random_int(self):
        return self.__random_int

    @abstractmethod
    def unique_attack(self):
        pass

    @abstractmethod
    def unique_scream(self):
        pass

    @abstractmethod
    def action(self):
        pass



# john = Hero(hp = 604, magical_attacks = ['water', 'stone', None, 'air'])
# john.protection()
# john.attack()
# john.rest()
# print(f'\nrandom integer number: {john.get_random_int()}')