counter = 0

class Heroes:

    def __init__(self, name = None, hp = 100, magical_attacks = None):
        global counter
        if name is None:
            self.name = 'user' + str(counter)
            counter += 1
        else:
            self.name = name

        self.hp = hp
        self.magical_attacks = magical_attacks

    def action(self):
        print(f"{self.name} performs an action.\n")

    def attack(self):
        attacks=['basic attack', 'charged attack','magical attack', 'poisonous attack', 'life-stealing attack']
        print(attacks)
        choice = input("choose an attack:")
        if choice == attacks[0]:
            print('the opponent is kicked!\n')
        elif choice == attacks[1]:
            import time
            print('the attack is charging up...')
            time.sleep(3)
            print('the opponent is punched!\n')
        elif choice == attacks[2]:
            if self.magical_attacks is None:
                print('you have no magic!\n')
            else:
                magics = []
                for magic in self.magical_attacks:
                    if magic is not None:
                        magics.append(magic)
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

count = 0

class Archer(Heroes):
    def __init__(self, name = None, hp = 100, arrows = 3, precision = 0):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision

    def attack(self):
        print('The shot was fired!\n')
        self.arrows -= 1
        if self.precision >= 5:
            print('successful shot!\n')
        else:
            print('missed shot!\n')

    def rest(self):
        self.arrows += 5
        print(f'arrows are replenished. quantity of arrows: {self.arrows}\n')

    def status(self):
        heros_status = f'name: {self.name}, hp: {self.hp}, arrows: {self.arrows}, precision: {self.precision}\n'
        return heros_status

            


# nanu = Heroes('nanuku')
# nanu.action()
# nanu.attack()

# oti = Heroes(magical_attacks=[None, None,'fire', 'air'])
# oti.action()
# oti.attack()

# mani = Archer('mani', precision = 3)
# mani.action()
# mani.attack()
# print(mani.status())
# mani.rest()
# print(mani.status())