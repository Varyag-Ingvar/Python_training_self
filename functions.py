def factorial(x):
    pr = 1
    for i in range(2, x + 1):
        pr = pr * i
    return pr


def sochet(n, k):
    return factorial(n) / factorial(k) * factorial(n - k)


print(sochet(5, 3))


def sq_and_per(a, b):
    return a * b, 2 * (a + b)


square, perimeter = sq_and_per(3, 5)  # присваиваем переменным значения возвращаемые функцией
print(square, perimeter)
