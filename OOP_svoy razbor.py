class Character:       # это Класс
    # name = ''          # это Атрибут класса
    # power = 0
    # energy = 100
    # hands = 2
    # backpack = []
    # Атрибут Класса, содержащий изменяемый тип данных, в данном случае список, будет ОБЩИМ для всех Экземпляров Класса
    # Чтобы этого избежать, надо использовать для инициализации Класса метод __init__
    def __init__(self, name, power, energy=100, hands=2):
        self.name = name
        self.power = power
        self.energy = energy
        self.hands = hands
        self.backpack = []
# теперь, все что мы не передали при инициализации (в скобках выше) будет работать уже для КОНКРЕТНОГО Экземпляра Класса



    def eat(self, food):         # это Метод класса (функции врутри класса называются методами)
        if self.energy < 100:
            self.energy += food
        else:
            print('Not hungry')


    def do_exercise(self, hours):     # каждый созданный в Классе Метод будет работать отдельно
        if self.energy > 0:           # для каждого Экземпляра Класса при вызове
            self.energy -= hours * 2
            self.power += hours * 2
        else:
            print('Too tired')

    def change_alias(self, new_alias):
        self.alias = new_alias


    def beat_up(self, foe):
        if not isinstance(foe, Character):
            return
        if foe.power < self.power:
            foe.status = 'Defeated'
            self.status = 'Winner'
        else:
            print('Retreat!')

peter = Character('Peter Parker', 80)         # это Экземпляр класса или Объект класса
# здесь в скобки необходимо передать параметры, которые не были инициализированы по умолчанию в методе __init__ Класса
# т.е. в данном случае это name и power
peter.alias = 'Spider-Man'  # это Атрибут Экземпляра Класса
peter.energy = 50
peter.hands = 8
# Атрибуты, заданные по умолчанию в момент инициализации класса, т.е. energy и hands,
# тоже могут быть изменены внутри конретного Экземпляра Класса прямым присвоением


# print(peter.name)
# print(peter.power)
# print(peter.energy)
# print(peter.hands)
# print(peter.alias)
# print('\n')


bruce = Character('Bruce Wayne', 90)    # создаем еще один Экземпляр класса (также передаем name, power в скобки)
bruce.alias = 'Batman'
bruce.energy = 70

# print(bruce.name)
# print(bruce.power)
# print(bruce.energy)
# print(bruce.hands)
# print(bruce.alias)

peter.do_exercise(2)  # вызываем метод Класса Character "do_exercise" конкретно для Экземпляра Класса "peter" (через.)
print(peter.energy)
print(peter.power)

peter.backpack.append('web_shooters')
print(peter.backpack)
print(bruce.backpack)
print(peter.hands)
print(bruce.hands)

bruce.beat_up(peter)
print(peter.status)
print(bruce.status)
