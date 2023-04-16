from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel

class Vehicle(ABC):
    started = False

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started:
            return
        if self.fuel == 0:
            raise LowFuelError()

        self.started = True

    def move(self, distance):
        if self.fuel < distance * self.fuel_consumption:
            raise NotEnoughFuel
        self.fuel -= distance * self.fuel_consumption
