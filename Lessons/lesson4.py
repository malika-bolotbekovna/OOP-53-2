# from abc import abstractmethod, ABC


# @staticmethod
# class Math(ABC):


#     @staticmethod
#     def add(a, b):
#         return a + b


# print(Math.add(3, 5))




# @classmethod
# class Person:

#     population = 0    # атрибут класса

#     def __init__(self, name):
#         self.name = name    # атрибут объекта класса
#         Person.population += 1

#     @classmethod
#     def get_population(cls):
#         return cls.population
    
# person1 = Person('Ardager')
# person2 = Person('Ardager2')

# print(Person.get_population())



# @property
# class Circle:

#     def __init__(self, radius):
#         self._radius = radius


#     @property   # превращает мето в атрибут вне клласса
#     def radius(self):
#         return 'property'
    
#     def radius2(self):
#         return 'just method'

# circle = Circle(5)
# print(circle.radius)   # without () 
# print(circle.radius2())      # with ()


# пример простого декоратора

# 3            def hello()
# def my_decorator(func):

#     # 4
#     def wrapper():
#         # 5
#         print('перед выполнением функции')
#         func()
#         print('после выполнения функции')

#     return wrapper

# # 2
# @my_decorator
# def hello():
#     print('hi!')

# # 1
# hello()




# декоратор с аргументом

# def repeat(n):
#     def decorator(func):
#         def wrapper():
#             for i in range(n):
#                 func()
        
#         return wrapper
#     return decorator

# amount = int(input('введите число: '))

# @repeat(amount)
# def greet():
#     print('hi!')

# greet()



# декораторы для класса
#            #    MyClass
# def class_decorator(cls):
#                #  MyClass
#     class NewClass(cls):
#         def new_method(self):
#             return 'new method'
        
#     return NewClass

# @class_decorator
# class MyClass:
    
#     def old_method(self):
#         return 'old method'
    

# obj = MyClass()

# print(obj.old_method())
# print(obj.new_method())