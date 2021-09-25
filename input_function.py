a=input()
#при таком вводе будет записываться тип данных - строка (str)
#чтобы преобразовать строку в целое число, используется функция int
#либо сразу пишется конструкция a=int(input())
a=int(a)
print(a)
print(type(a))

#для преобразования в другие типы данных используется таже конструкция, см.пример ниже
c=float(input())
print(c)
print(type(c))

#периметр треугольника
print("let's calculate triangle perimeter")
a=float(input("enter value a: "))
b=float(input("enter value b: "))
c=float(input("enter value c: "))
#округлим ответ до сотых
p=(round(a+b+c, 2))
print("triangle perimeter is: ", p)