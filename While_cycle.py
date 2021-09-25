# i = 1
# while i<5:
#     print(i)
#     i=i+1
#
# i = 2
# while i<5000:
#     print(i)
#     i=i*2
#
# n = int(input("Enter a mumber: "))
# i = 1
# while i<n+1:
#     print("Hello")
#     i=i+1
#
# x=20
# while x>=10:
#     print(x)
#     x=x-1

guess = input("Enter password: ")
password = "qwerty"
count = 0
while guess != password:
    count += 1
    print("Invalid password! Try again!")
    guess = input()
print(f"Вы потратили {count} попыток!")

a = [2,3,5,6,4,5,3,54,3,55,25,41,3]
print(a)

while 3 in a:    # удаляем все тройки из списка а.
    a.remove(3)
    print(a)     # если print внутри цикла (с табуляцией) то мы увидим все промежуточные результаты
print(a)         # если выведем из цикла (без отступа, по линии с while), то получим сразу конечный

s = "privet"
while len(s)>0:
    print(s[0])
    s=s[1: ]

str_1 = "sghdkHHyNJgfd#$%^23564" # разбираем с помощью цикла while строку по-символьно с указанием сути каждого символа
while len(str_1) > 0:
    bukva = str_1[0]
    if "a" <= bukva <= "z":
        print(bukva, "small")
    elif "A" <= bukva <= "Z":
        print(bukva, "big")
    elif bukva.isdigit():
        print(bukva, "digit")
    else:
        print(bukva, "sign")
    str_1 = str_1[1: ]