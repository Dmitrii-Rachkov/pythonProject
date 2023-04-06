class Car():

    def __init__(self, model, year, engine, price, mileage):
        self.model = model
        self.year = year
        self.engine = engine
        self.price = price
        self.mileage = mileage
        self.wheel = 4

    def description_car(self):
        print(f"Модель: {self.model}, Год: {self.year}, Объём: {self.engine}, Цена: {self.price}, "
              f"Пробег: {self.mileage}, Колёса: {self.wheel} ")


toyota = Car("Toyota", 2021, 2.5, 5000000, 10000)
toyota.description_car()


class Truck(Car):
    def __init__(self, model, year, engine, price, mileage):
        super().__init__(model, year, engine, price, mileage)
        self.wheel = 8


kamaz = Truck("Kamaz", 2020, 10.5, 8000000, 15000)
kamaz.description_car()
