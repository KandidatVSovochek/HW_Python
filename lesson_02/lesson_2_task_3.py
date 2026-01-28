import math


def square(side):
    return math.ceil(side*side)


a = float(input("Введите размер стороны квадрата "))
result = square(a)
print(result)
