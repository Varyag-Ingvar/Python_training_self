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

    with open(file_name) as file:
        data = {}                      # создаем пустой словарь
        for line in file:
            shop_name = line.strip()   # первая итерация записывается в shop_name
            counter = int(file.readline()) # забираем вторую строку из файла, т.е. цифру 2, т.е. кол-во строк с машинами в первом салоне
            # print(line.strip())      # .strip выводит строки, полученные в результате итерации по файлу без пробелов

            temp_list = []                # создаем временный пустой список
            for item in range(counter):   # вложенным циклом бежим по полученному кол-ву строк в салоне
                # car = file.readline()   # присваиваем переменной car каждую строку с машинами в каждом салоне
                name, color, quantity = file.readline().split('|') # множественным присвоением записываем название, цвет, количество в переменные
                temp_list.append(
                    {'Car_name': name, 'color': color, 'quantity': quantity}
                )
            data[shop_name] = temp_list # записываем в словарь data ключ - название салона, значения - списки словарей вида {'Car_name': name, 'color': color, 'quantity': quantity}
            file.readline()             # !берем строку с пробелом в файле между салонами, чтобы избежать ошибки, иначе первый цикл натыкается на пробел, в котором нет цифр!
    return data

print(get_data('api.txt'))