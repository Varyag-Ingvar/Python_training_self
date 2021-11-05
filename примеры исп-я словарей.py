# d = {}
# d['a']=1
# print(d)
# if 'a' in d:
#     d['a'] += 1
# else:
#     d['a'] = 1
# print(d)
# if 'b' in d:
#     d['b'] += 1
# else:
#     d['b'] = 1
# print(d)

# ниже скрипт для подсчета введенных пользователем символов (букв, цифр, знаков) в виде словаря
s = input("Let's count how many times you enter the same letter or symbol:\n")
d = {}
for i in s:
    # if i.isalpha(): если хотим выводить только буквы
    # if i.isdigit(): если хотим выводить только цифры
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
    # d[i] = d.get(i, 0) + 1  такой строкой можно заменить проверки выше
print(d)
for i in sorted(d):
    print(i,d[i])    # перебираем ключи в словаре и выводим пару ключ-значение

# программка, которая при вводе слова просит ввести его перевод, и записывает рез-т в словарь в виде пары: ключ-значение
# или выводит слово и его перевод, если таковые уже в ней были записаны
words = {}
while True:
    k = input("Введите англ.слово, которое хотите перевести (or type 'exit' to exit the program): ")
    if k == 'exit':
        break
    if k in words:
        print(f"Слово '{k}' переводится как '{words[k]}'")
    else:
        print(f"Введите перевод слова {k}: ")
        words[k] = input()

