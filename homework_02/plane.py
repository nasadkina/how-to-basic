"""
создайте класс `Plane`, наследник `Vehicle`
"""


from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0
    max_cargo = 0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        Vehicle.__init__(self, weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, new_cargo):
        if self.cargo + new_cargo > self.max_cargo:
            raise CargoOverload
        self.cargo += new_cargo


    def remove_all_cargo(self):
        cur_cargo = self.cargo
        self.cargo = 0
        return cur_cargo

