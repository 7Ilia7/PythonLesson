class Person():
    """Создаем человека"""

    def __init__(self, name, age, height):
        """"Инициализируем атрибуты человека"""
        self.name = name
        self.age = age
        self.height = height
        self.weight = 100

    def description_person(self):
        """Получение описания человека"""
        description = self.name + " ему " + str(self.age) + ", его рост " + str(self.height) + " см " + "и его вес " + str(self.weight) + "кг!"
        print("Нового челоека зовут: " + description)

    def get_weight(self):
        """Получение веса человека"""
        print("Вес вашего человека " + str(self.weight))

    def update_weight(self, kg):
        """Изменение веса человека"""
        self.weight = kg

# class Warrior(Person):
#     """"Создаем класс воина"""
#
#
#     def __init__(self, name, age, height):
#         """Инициализируем атрибуты класс родителя"""
#         super().__init__(name, age, height)
#         self.rage = 100
#
#     def get_rage(self):
#         """Получение заряд ярости"""
#         print("заряд ярости равен: " + str(self.rage))
#
#     def description_person(self):
#         """Переопределения метода родителя"""
#         description = self.name + " ему " + str(self.age) + ", его заряд ярости:" + str(self.rage)
#         # print("Нового челоека зовут: " + description)
#         return description


# warrior = Warrior("Ilia", 32, 200)
#
# print("Нового челоека зовут: " + warrior.description_person())


# man = Person("Illia", 30, 176)
# man.description_person()