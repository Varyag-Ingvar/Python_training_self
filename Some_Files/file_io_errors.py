from pprint import pprint

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
                    {'car_name': name.strip(), 'color': color, 'quantity': quantity}
                )
                # важно для домашки тут .strip() после name
            data_1[shop_name] = temp_list # записываем в словарь data в виде: ключи - название салона, значения - списки словарей вида {'Car_name': name, 'color': color, 'quantity': quantity}
            file_1.readline()             # !берем строку с пробелом в файле между салонами, чтобы избежать ошибки, иначе первый цикл натыкается на пробел (и не сможет привести пробел к целому числу)!
    return data_1

pprint(get_data('api.txt'))


def find_by_name(car_name, data):
    for shop in data.values():
        for car in shop:
            if car['car_name'] == car_name:
                print(f'car {car_name} is in stock')

find_by_name('KIA', get_data('api.txt'))
print('')

data_2 = get_data('api.txt')
# data_3 = data_2['Salon']     # специально вызываем ошибку KeyError (такого ключа - Salon в нашем словаре нет)
# pprint(data_3)

try:
    data_3 = data_2['Salon']   # ловим ошибку
except KeyError:
    print('No such key!')

print('')

try:
    12/0
except Exception as error:  # при использовании Exception в принте выдаст название ошибки
    print(error)