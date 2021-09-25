# методы для строк

print("hello".upper())

print("HELLO".lower())

# count считает сколько таковых символов в строке (чувств. к регистру!!!)
s = "HELLO"
print(s.count("L"))
print(s.count("E"))

# для нахождения индекса символа в строке используется find
print(s.find("L"))
print(s.find("E"))

# index работает аналогично find
print(s.index("O"))

# replace заменяет символы в строке
print(s.replace("L", "i")) # меняем обе L на i

# isalpha и isdigit проверяет, состоит ли ВСЯ строка из букв или цифр
print(s.isalpha())
print(s.isdigit())

name = "ivanov ivan ivanovich"
num = "23,256,325,188,154,12"
print(name.split()) # split превращает строку в список
print(num.split(",")) # отделили числа в строке в список через запятую (",")
abc = num.split(",")
print(",".join(abc)) # вернули список к виду строки через разделитель ","
print("+".join(abc))