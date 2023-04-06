class Hero():

    def __init__(self, name, helth, mana, energy):
        self.name = name
        self.helth = helth
        self.mana = mana
        self.energy = energy
        self.element = "Fire"

    def description_hero(self):
        print(f"Герой: {self.name}, здоровье: {self.helth}, мана: {self.mana},"
              f" энергия: {self.energy}, стихия: {self.element}")

    def update_element(self, new_element):
        self.element = new_element







