from abc import ABC, abstractmethod
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        print("Атакуем: рубит  мечом")

class Bow(Weapon):
    def attack(self):
        print("Атакуем: стреляет из  лука стрелами")



class Fighter():
    def __init__(self, name, age, weapon: Weapon):
        self.name = name
        self.age = age
        self.weapon = weapon

    def changeWeapon(self, new_weapon: Weapon):
        self.weapon = new_weapon

    def att(self):
        print(f"Воин {self.name}  Атакует")
        self.weapon.attack()


class Monster():
    def __init__(self, name, age):
        self.name = name
        self.age = age


sw1 = Sword()
b1 = Bow()

voin = Fighter("Илья Муромец",33, sw1)
raz1 = Monster("Соловей Разбойник", 300)
raz2 = Monster("Кащей", 1000)

print(f"Воин {voin.name}  сражается с  {raz1.name}")
voin.att()
print(f"   {raz1.name} повержен ")

print(f"Воин {voin.name}  берет лук")
voin.changeWeapon(b1)

print(f"Воин {voin.name}  сражается с  {raz2.name}")
voin.att()
print(f"   {raz2.name} повержен ")


