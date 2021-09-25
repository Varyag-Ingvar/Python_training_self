a = list(range(5))              # арифм.прогрессия
print(a)

b = list(range(10, 100))
print(b)

c = list(range(10, 100, 10))    # от какого числа, до какого , шаг
print(c)
print(len(c))                   # длина прогрессии (кол-ыо символов в ней)

d = list(range(10, 0, -1))
print(d)

e = sum(range(1, 101))         # сумма арифметической прогрессии (от 1 до 100), берем в конце плюс один всегда!
print(e)


x,y,z = range(0, 3)            # множественное присвоение, т.е. в кажд.переменную через запятую пойдет по 1 числу прогрессии
print(x)
print(y)
print(z)

v = iter(range(5))
print(v.__next__())            # next проходится по каждой итерацииб в данном случае от 0 до 4
print(v.__next__())
print(v.__next__())
print(v.__next__())
print(v.__next__())

n = iter([256, True, "Salam"]) # next позволяет проходится по спискам (по любым итерируемым объектам)
print(n.__next__())
print(n.__next__())
print(n.__next__())