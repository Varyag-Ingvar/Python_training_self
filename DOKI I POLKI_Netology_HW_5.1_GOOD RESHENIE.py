documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }


def get_people(document):
    doc_number = input("Введите номер документа: ")

    doc_len = len(document)
    for key, value in enumerate(document):
        if value["number"] == doc_number:
            return value["name"]

    if doc_len == len(document):
        return "Такого документа не существует"


def get_shelf(directory):
    num_doc = input("Введите номер документа: ")

    for Shelf_number in directory:
        if num_doc in directory[Shelf_number]:
            return Shelf_number
    return "Такого документа не существует"


def get_list(document):
    result_list = ""
    for people in document:
        result = " ".join(f"{value}" for key, value in people.items())
        result_list += result + "\n"
    return result_list


def get_add(document, directory):
    which_shelf = input("Введите номер полки: ")
    if which_shelf in directory.keys():
        type_doc = input("Введите наименование документа: ")
        doc_number = input("Введите номер документа: ")
        name_people = input("Введите Имя и Фамилию: ")
        new_people = dict(type=type_doc, number=doc_number,
                          name=name_people)
        document.append(new_people)
        list_doc = directory[which_shelf]
        list_doc.append(doc_number)
        directory[which_shelf] = list_doc
    else:
        print("Полка с таким номером не существует!")
        get_add(document, directory)
    return f"{document}, \n {directory}"


def get_delete(document, directory):
    doc_number = input("Введите номер документа: ")

    doc_len = len(document)
    for key, value in enumerate(document):
        if value["number"] == doc_number:
            document.pop(key)

    if doc_len == len(document):
        return "Такого документа не существует!"

    for value_list in directory.values():
        for doc in value_list:
            if doc_number == doc:
                value_list.remove(doc)

    print(document, directory)
    return "Документ успешно удален"


def get_move(directory):
    num_doc = input("Введите номер перемещаемого документа: ")
    num_shelf = input("Введите номер полки, на которую переместить "
                      "документ: ")

    doc_existence = False

    if num_shelf not in directory:
        return "Такой полки не существует!"

    for shelf_number, doc_number in directory.items():
        if num_doc in doc_number:
            doc_existence = True
            directory[num_shelf] += [num_doc]
            doc_number.remove(num_doc)

    if doc_existence:
        print(directory)
        return "Документ успешно перемещен"
    else:
        return "Такой документ не существует!"


def get_add_shelf(directory):
    num_new_shelf = input("Введите номер новой полки: ")

    if num_new_shelf in directory:
        print(directory)
        return "Такая полка уже существует!"

    directory[num_new_shelf] = []

    return directory


def main(document, directory):

    print("Список команд:\n 1. p - Запрашивает номер документа и "
          "выведет имя человека, которому он принадлежит.\n "
          "2. s - Запрашивает номер документа и выводит номер полки, "
          "на которой он находится.\n 3. l - Выведет список "
          "всех документов.\n 4. a - Добавит новый документ в список "
          "и в перечень полок, спросив его номер, тип, имя владельца и номер "
          "полки, на котором он будет храниться.\n 5. d - Запросит "
          "номер документа и удалит его из списка документов и из перечня полок.\n "
          "6. m - Запросит номер документа и целевую полку и "
          "переместит его с текущей полки на целевую.\n 7. as - "
          "Запросит номер новой полки и добавит ее в перечень.\n 8. q - Выход")

    while True:
        user_input = input('Введите команду (p, s, l, a, d, m, as, q) - ')
        if user_input == 'p':
            print(get_people(document))
        elif user_input == 's':
            print(get_shelf(directory))
        elif user_input == 'l':
            print(get_list(document))
        elif user_input == 'a':
            print(get_add(document, directory))
        elif user_input == 'd':
            print(get_delete(document, directory))
        elif user_input == 'm':
            print(get_move(directory))
        elif user_input == 'as':
            print(get_add_shelf(directory))
        elif user_input == 'q':
            break
        else:
            print("Неверная команда! Повторите ввод!")


main(documents, directories)

