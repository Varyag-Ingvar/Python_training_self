class Character:
    def __init__(self, name, power, energy=50, hands=2):
        self.name = name
        self.power = power
        self.energy = energy
        self.hands = hands

class Spider:
    def __init__(self, power, energy=30, hands=8):
        self.power = power
        self.name = name
        self.hands = hands

    def webshoot(self):
        print('Pew-Pew!')

class SpiderMan(Character, Spider):
    pass

peter_parker = SpiderMan('Peter Parker', 80)
print(peter_parker.name)
print(peter_parker.power)
print(peter_parker.energy)
print(peter_parker.hands)
peter_parker.webshoot()