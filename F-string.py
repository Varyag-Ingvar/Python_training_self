name = "Nikolai"
last_name = "Otmorozok"
acc_balance = 1958.50
text = f"Dear {name} {last_name}, your account balance is {acc_balance} dollars"
print(text)

# в фигурных скобках можно выполнять математические операции и применять методы.

text_1 = f"Dear {name.upper()} {last_name.lower()}, your account balance is {acc_balance * 2 - 25} dollars"
print("\n")
print(text_1)

# пример использования со словарём и списком
# сначала пишем словарь:
gender = {
    'm': 'Дорогой',
    'f': 'Дорогая'
}
# пишем вложенный список:
client_names = [
    ['Evgeniy', 'Victorovich', 35.58, 'm'],
    ['Oksana', 'Nikolaevna', 24.33, 'f'],
    ['Igor', 'Markovich', 75357.55, 'm'],
]
# пишем цикл for:
for name, midname, balance, g in client_names:
    text = f"{gender[g]} {name} {midname}, баланс вашего счета составляет {balance} евро"
    print(text)