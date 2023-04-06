from legend_oop import *


class Mag(Hero):

    def __init__(self, name, helth, mana, energy, race):
        super().__init__(name, helth, mana, energy)
        self.race = race
        self.color = "Black"

    def get_race_color(self):
        return f"Расса: {self.race}, Цвет: {self.color}"

    def update_race_color(self, race, color):
        self.race = race
        self.color = color

    def new_element(self, element):
        self.element = element

    def description_hero(self):
        print(f"Герой: {self.name}, здоровье: {self.helth}, мана: {self.mana},"
              f" энергия: {self.energy}, стихия: {self.element}, расса: {self.race}, "
              f"цвет: {self.color}")

        """У нас в родительском классе 'Hero' есть метод 'description_hero'
        и мы можем переопределить этот метод в нашем потомке. Пример выше.
        В родительском классе метод остаётся без изменений."""


hero_1 = Mag("Emma", 100, 120, 150, "Russian")
hero_1.description_hero()
print(hero_1.get_race_color())
"""Также можем использовать 'return' в методах чтобы возвращать результат."""
hero_1.update_race_color("USA", "Greengo")
hero_1.new_element("Water")
hero_1.description_hero()
