# 4.1

def check_type(func):
    def wrapper(x):
        if not isinstance(x, (int, float)):
            return "Ошибка: ожидалось число"
        return func(x)
    return wrapper


@check_type
def square(x):
    return x * x

print(square(5))     
print(square("hi"))  
print(square([1, 5, -5, 3.4]))  
print(square({}))  



# 4.2

def count_calls(func):
    wrapper_calls = 0
    def wrapper(*args, **kwargs):   # на случай, если func принимает аргументы
        nonlocal wrapper_calls
        wrapper_calls += 1
        print(f'функция вызвана {wrapper_calls} раз')
        return func(*args, **kwargs)
    return wrapper


@count_calls
def hello():
    print("Привет!")

hello()
hello()
hello()


@count_calls
def multiplication(a, b):
    return a * b

print(multiplication(2.4, -5))     
print(multiplication(10, 23))   
print(multiplication(0, 123))     
