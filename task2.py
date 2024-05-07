class Vehicle:
    vehicle_type = "none"


class Car:
    price = 1000000

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Цена {}'.format(self.__class__.price)

    def horse_powers(self):
        print('Колличество лошадинных сил 150')


class Nissan(Vehicle, Car):
    vehicle_type = "Nissan"
    price = 800000

    def horse_powers(self):
        print('Колличество лошадинных сил 140')


obj = Nissan(name=Nissan)

print(obj.vehicle_type, 'Цена', obj.price)
obj.horse_powers()
