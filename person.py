class Person():
    """"Модель человека"""

    def __init__(self, name, age):
        """"Инициализация атрибутов человека - имя, возвраст"""
        self.name = name
        self.age = age
        print("Человек создан")

    def sing(self):
        """"Просим человека спеть"""
        print(self.name + " поет")

    def dance(self):
        """"Просим человека станцевать"""
        print(self.name + " танцует")

man = Person("Алекс", 30)
woman = Person("Lena", 25)
print(man.name)

man.dance()
woman.sing()