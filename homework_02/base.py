from abc import ABC

from homework_02 import exceptions

'''
- доработайте базовый класс `base.Vehicle`:
    - добавьте атрибуты `weight`, `started`, `fuel`, `fuel_consumption` со значениями по умолчанию
    - добавьте инициализатор для установки `weight`, `fuel`, `fuel_consumption`
    - добавьте метод `start`. При вызове этого метода необходимо проверить состояние `started`. 
    И если не `started`, то нужно проверить, что топлива больше нуля, 
      и обновить состояние `started`, иначе нужно выкинуть исключение `exceptions.LowFuelError`
    - добавьте метод `move`, который проверяет, 
      что топлива достаточно для преодоления переданной дистанции (вплоть до полного расхода), 
      и изменяет количество оставшегося топлива, иначе выкидывает исключение `exceptions.NotEnoughFuel`
'''


class Vehicle(ABC):

    def __init__(self, weight=1_467, fuel=50, fuel_consumption=10):
        self.fuel_consumption = fuel_consumption
        self.fuel = fuel
        self.weight = weight
        self.started = False

    def start(self):
        if not self.started:
            if self.fuel <= 0:
                msg = 'cannot_start'
                raise exceptions.LowFuelError(msg)
            self.started = True

    def move(self, distance):
        if self.fuel < self.fuel_consumption * distance:
            raise exceptions.NotEnoughFuel
        self.fuel -= self.fuel_consumption * distance
