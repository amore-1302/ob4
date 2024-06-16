from abc import ABC, abstractmethod
class Fighter():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Monster():
    def __init__(self, name, age):
        self.name = name
        self.age = age


voin = Fighter("Илья Муромец",33)
raz = Monster("Соловей Разбойник", 300)
print(voin)
print(raz)