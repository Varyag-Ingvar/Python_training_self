a = [43,65,3,54,6]

# for i in a:
#     print(i, a.index(i))  # обход по значениям

n = len(a)
for i in range(5):          # обход по индексам
    print(i, a[i])
    a[i]+=5
print(a)

for i in range(3):
    for j in range(5):
        print("*", end="")
    print()

# программа ниже перебирает все возможные сочетания ТРЕХ значений
# из всех возможных символов на клавииатуре

# from string import printable
#
# print(printable)
#
# for b1 in printable:
#     for b2 in printable:
#         for b3 in printable:
#             print(b1,b2,b3)

# Таблица умножения
for i in range (1,10):
    for j in range(1,11):
        print(i, "*",j, "=",i*j,end="  ")
    print()


