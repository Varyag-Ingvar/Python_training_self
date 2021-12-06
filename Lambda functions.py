# lambda functions (анонимные функции)

# функция возвращает квадрат числа x
def f(x):
    return x**2

# таже запись в виде анонимной функции
r = lambda x: x**2 #

print(r(7))


# периметр треугольника
def perimeter(a, b, c):
    p = a + b + c
    return p

# таже запись в виде анонимной функции
per = lambda a,b,c: a+b+c

print(per(1,2,3))


def f(num):
    if num > 0:
        return 'Positive'
    else:
        return 'Negative'

t = lambda num: 'Positive' if num>0 else 'Negative'

print(t(5))


# функция, которая возвращает функцию lambda
def linear(k,b):
    return lambda x: x*k+b

graf1 = linear(2,5)   # записываем первую функцию в переменную, передаем в нее два значения - k,b
print (graf1(3))      # вызываем функцию из переменной и передаем значение - x