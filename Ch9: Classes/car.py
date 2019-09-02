class Car:
    def __init__(self, make, model, year):
        ''' A simple attempt to represent a car..'''
        self.make = make
        self.model = model
        self.year = year

        ''' To make the class more interesting, let's add an attribute that changes
            over time.'''
        ''' When an instance is created, attributes can be defined without being passed
            in as parameters. These attributes can be defined in the __init__() method,
            where they are assigned a default value.'''
        self.odometer_reading = 0


    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


    def read_odometer(self):
        ''' Print a statement showing the car's mileage.'''
        print(f"This car has {self.odometer_reading} miles on it.")


    def update_odometer(self, mileage):
        ''' Set the odometer reading to the given value.
            Reject the change if it attempts to roll the odometer back.'''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    
    def increment_odometer(self, miles):
        ''' Add the given amount to the odometer reading.'''
        self.odometer_reading += miles


my_new_car = Car("audi", "a4", 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# Modifying an attribute's value directly
my_new_car.odometer_reading = 22
my_new_car.read_odometer()

# Modifying an attribute's value through a method.
my_new_car.update_odometer(23)
my_new_car.read_odometer()

# Incrementing an attribute's value through a method
my_used_car = Car("sabaru", "outback", 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()