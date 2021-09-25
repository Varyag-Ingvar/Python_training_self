#множественное присвоение

a=b=c=d=5
print(a)
print(b)
#etc

a, b, c = 5, 7, 9
print(a)
print(b)
print(c)

#меняем значения (объекты) в переменных местами
a=2
b=5
print(a, b)
a, b = b, a
print(a, b)