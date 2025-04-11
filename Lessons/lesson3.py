# from abc import ABC, abstractmethod
#
#
# class Animal(ABC):
#
#     @abstractmethod
#     def make_sound(self):
#         pass
#
#     @abstractmethod
#     def move(self):
#         pass
#
#
#
# class Dog(Animal):
#     def make_sound(self):
#         return "Gaf gaf"
#
#     def move(self):
#         return  "action step"
#
# dog = Dog()
#
# print(dog)
# print(dog.make_sound())
# print(dog.move())
#
#



# class Vector:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
#     # def __str__(self):
#     #     return 'New print'
#
#     def __lt__(self, other):
#         return "New lt"
#
#
#     def __eq__(self, other):
#         return  f"{self.x} ------ {other.x}"
#
#
# vector1 = Vector(12,12)
# vector2 = Vector(33,33)
#
#
# print(vector1 == vector2)

class Animal:

    def action(self):
        return 'Animal action'



class Swimmable(Animal):
    def action(self):
        return "Плавать"


class Flyable(Animal):
    def action(self):
        return "Летит"




class Duck(Swimmable, Flyable):
    def make_sound(self):
        return 'Кря кря'


donald_duck = Duck()

print(donald_duck.action())