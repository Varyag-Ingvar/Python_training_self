# enumerate function

a = [10, 20, 30, 40, 50, 60]
s = 'hello'
t = ('apple', 'banana', 'mango')


print(list(enumerate(a)))

# for couple in enumerate:
#     print(couple)

# циклом можем обходить по отдельности индекс и значения списков, строк, кортежей, передаваемых в функцию enumerate
for index, value in enumerate(a):
    print(index, value)

for index, value in enumerate(s):
    print(index, value)

# значение первого порядкового номера можно задать через запятую (т.е. в данном случае начнем с единицы)
for index, value in enumerate(t, 1):
    print(index, value)
