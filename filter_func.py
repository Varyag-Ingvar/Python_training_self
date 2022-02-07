
def fu(x):
    if x>10:
        return True
    else:
        return False


# т.к. результат сравнения всегда выдает булево значение, то функция выше пишется в две строки:
def foo(x):
    return x>10


a = [14, 0, 5, 79, 645, 7952, 18, 3, 192, 471]

# далее фильтруем наш список а, используя функцию foo, передавая их в функцию filter
b = sorted(list(filter(foo, a)))
print(b)

# отфильтруем только четные числа списка а
def even(y):
    return y%2==0

c = sorted(list(filter(even, a)))
print(c)


#  отфильтруем только двузначные числа
def xx(z):
    return 9 < z < 100

d = sorted(list(filter(xx, a)))
print(d)

# тоже самое с использованием list comprehension
e = sorted([i for i in a if 9 < i < 100])
print(e)

# уберем из списка пустые значения с помощью функции bool
# т.е. в данном случае из списка а удалятся нули
# в функцию filter можно также передать None, результат будет тот же
f = sorted(list(filter(bool, a)))
print(f)

# при помощи анонимной функции фильтруем список по длине строки
text_list = ['worm', 'hi', 'low', 'smash', 'parrot', 'maniac']
g = sorted(list(filter(lambda x: len(x)>=4, text_list)))
print(g)

# фильтруем строку
str_1 = '368jgddsHJKffFFGH256z'
filtered_str_1 = list(filter(str.isdigit, str_1))
filtered_str_2 = list(filter(str.isalpha, str_1))
filtered_str_3 = list(filter(str.isupper, str_1))
print(filtered_str_1)
print(filtered_str_2)
print(filtered_str_3)

# фильтруем словарь по ключам или значениям, в данном примере по значениям
dict_1 = {
    'moscow': 800,
    'kiev': 750,
    'LA': 400,
    'NY': 900,
    'Chicago': 650
}
#  получим список ключей словаря (городов), значение которых больше 700
filt_dict = list(filter(lambda x: dict_1[x] > 700, dict_1))
print(filt_dict)


