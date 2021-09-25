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


def get_name_from_pass_number(documents_base):
    doc_num = input("Enter passport number: ")
    for client in documents_base:
        if client["number"] == doc_num:
            return client["name"]
    return "Invalid document number. Please re-enter."


name_search = get_name_from_pass_number

# print(name_search)


def get_shelf_from_pass_number(directories_base):
    doc_num = input("Enter passport number: ")
    for k,v in directories_base.items():
        # print(k,v)
        if doc_num in v:
            return k
    return "Invalid document number. Please re-enter."


shelf_search = get_shelf_from_pass_number

# print(shelf_search)


def get_all_docs_list(doc_list_base):
    docs_list = []
    for z in doc_list_base:
        doc_type = z["type"]
        doc_number = z["number"]
        client_name = z["name"]
        docs_list.append(f'{doc_type} "{doc_number}" "{client_name}"')
    return docs_list


docs_l = get_all_docs_list




# def add_new_doc(doc_add):
#     for z in doc_add:
#         z["type"] = input("")
#         doc_number = z["number"]
#         client_name = z["name"]
#         docs_list.append(f'{doc_type} "{doc_number}" "{client_name}"')
#     return docs_list







my_func_dict = {"p": name_search, "s": shelf_search, "l": docs_l }

x = input("Enter a command: ")
if x == "p":
    print(my_func_dict["p"](documents))
elif x == "s":
    print(my_func_dict["s"](directories))
elif x == "l":
    print(my_func_dict["l"](documents))
