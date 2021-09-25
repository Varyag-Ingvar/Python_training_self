file = open('data.txt')
# print(type(file))
#
data = file.read()
print(data)
# print(type(data))
#
file.close()

print(f'данные из файла все еще присутствую в переменной data - {data}')


def is_closed(file_obj):     # функция проверяет открыт файл или закрыт
    if file_obj.closed:
        print('File closed')
    else:
        print('File opened')


# with open('data.txt') as file:  # менеджер контекста - with as позволяет автоматически закрывать файл после работы с ним
#     print(type(file))
#     print(file.read())
#     is_closed(file)


def get_file_data(file_name):     # упакуем конструкцию with as в функцию
    with open(file_name) as file:
        return file.read()


data = get_file_data('data.txt')
print(data)
is_closed(file)
