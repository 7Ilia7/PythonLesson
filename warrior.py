from base_person import Person

warrior = Warrior("Ilia", 32, 200)
print("Нового челоека зовут: " + warrior.description_person())

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