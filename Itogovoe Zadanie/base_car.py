class Car():
    """Добавляем атрибты класса"""
    def __init__(self, model, age, cub, price, mileage, numberOfWheel):
        self.model = model
        self.age = age
        self.cub = cub
        self.price = price
        self.mileage = mileage
        self.numberOfWheel = 4

    def description_car(self):
        """Получение описания автомобиля"""
        description = self.model + "\n год выпуска-" + str(self.age) + ", обьем двигателя-" + str(self.cub) + ", пробег-" + str(self.mileage) + ", цена-" + str(self.price) + ", Количество колес-" + str(self.numberOfWheel)
        print("Описание машины: " + description)

    def get_cub(self):
        """Получение обьема двигателя"""
        print("Вес вашего человека " + str(self.cub))

    def update_mileage(self, kg):
        """Изменение пробега"""
        self.mileage = km

# name = Car("Megan",2012, 1500, 7000, 242000, 4)
# name.description_car()
#
truck = Car("Volvo",2012, 1500, 7000, 454332, 8)
truck.description_car()