"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class VehicleException(Exception):
    pass


class LowFuelError(VehicleException):
    pass


class NotEnoughFuel(VehicleException):
    pass


class CargoOverload(VehicleException):
    pass
