from car import Car
from electric_car import ElectricCar

my_new_car = Car("audi", "a4", 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()


my_tesla = ElectricCar("tesla", "model x", 2020)
print(my_tesla.get_descriptive_name())