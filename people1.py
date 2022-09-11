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



man = Person("Illia", 30, 176)

man.description_person()
man.weight = 110

man.update_weight(120)
man.get_weight()