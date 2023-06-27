"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle

from homework_02.engine import Engine


class Car(Vehicle):

    def __init__(self, weight=1_467, fuel=50, fuel_consumption=10):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = None

    def set_engine(self, engine: "Engine"):
        self.engine = engine
