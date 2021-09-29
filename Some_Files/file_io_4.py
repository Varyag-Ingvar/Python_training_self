# в этом примере будем работать с файлами, которые лежат в других каталогах

import os  # импортируем библиотеку os для работы с др.каталогами

with open('api.txt') as file:
    data = file.read()        # информация из файла сохраняется в переменной data в виде строки
    print(data, '\n')

with open('api.txt') as file:
    data = file.readline()      # readline получает первую строку из файла api.txt
    print(data, '\n')

with open('api.txt') as file:
    data = file.readlines()      # readlines получает список строк
    print(data, '\n')
    print(data[-1], '\n\n')        # по индексу вызываем посл.строку из списка


def get_data(file_name):

    with open(file_name) as file_1:
        data_1 = {}                      # создаем пустой словарь
        for line in file_1:
            shop_name = line.strip()   # первая итерация записывается в shop_name
            counter = int(file_1.readline()) # забираем вторую строку из файла, т.е. цифру 2, т.е. кол-во строк с машинами в первом салоне
            # print(line.strip())      # .strip выводит строки, полученные в результате итерации по файлу без пробелов

            temp_list = []                # создаем временный пустой список
            for item in range(counter):   # вложенным циклом бежим по полученному кол-ву строк в салоне
                # car = file.readline()   # присваиваем переменной car каждую строку с машинами в каждом салоне
                name, color, quantity = file_1.readline().split('|') # множественным присвоением записываем название, цвет, количество в переменные и сплитуем строку в список с разделителем |
                temp_list.append(
                    {'Car_name': name, 'color': color, 'quantity': quantity}
                )
            data_1[shop_name] = temp_list # записываем в словарь data в виде: ключи - название салона, значения - списки словарей вида {'Car_name': name, 'color': color, 'quantity': quantity}
            file_1.readline()             # !берем строку с пробелом в файле между салонами, чтобы избежать ошибки, иначе первый цикл натыкается на пробел (и не сможет привести пробел к целому числу)!
    return data_1

# print(get_data('api.txt'))

# РЕЖИМЫ доступа к файлам:
# 'r' - read (by default)
# 'w' - write (rewrite the whole file)
# 'a' - write info in the end of file (дозапись в конец файла)

# РЕЖИМЫ чтения/записи
# 'b' - двоичный режим
# 't' - текстовый режим (по умолчанию)

def read_data(file_name, encoding):         # функция открывает файл для чтения
    with open(file_name, 'r', encoding=encoding) as file:
        data = file.read()
        return data

# def write_data(file_name, text):   # функция записи в файл, информация в файле полностью перезапишется при вызове функции
#     with open(file_name, 'w') as file:
#         file.write(text)

# параметр encoding используется для указания кодировки файла (напр.UTF-8)
def write_to_data(file_name, mode, encoding, text):   # функция ДОзаписи в файл, информация в файле ДОзапишется при вызове функции
    with open(file_name, mode, encoding=encoding) as file:
        file.write(f'{text} \n')

# write_data('file.txt', 'Hello, Java')
# print(read_data('file.txt'))

# file_name = 'file.txt'
# path = f'{os.getcwd()}\{file_name}'  # получаем путь к нашему файлу
# print(path)

# write_to_data('file.txt', 'a', 'Hello, Python')
# print(read_data('file.txt'))

# write_to_data(path, 'a', 'Hello, Python')
# print(read_data(path))

file_name_cp = 'cp.txt'
file_name_utf = 'utf.txt'

path_cp = f'{os.getcwd()}\{file_name_cp}'  # получаем путь к нужному файлу
path_utf = f'{os.getcwd()}\{file_name_utf}'

print(path_cp)
print(path_utf)
print('')

write_to_data(path_cp, 'w', 'cp1251', 'Hello, Python')
write_to_data(path_cp, 'w', 'utf-8', 'Hello, Python')
print(read_data(path_cp, 'cp1251'))
print(read_data(path_utf, 'utf-8'))