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


    def fill_gas_tank(self):
        print("Filled gas tank.")


class Battery:
    '''A simple attempt to model a battery for an electric car.'''

    def __init__(self, battery_size=75):
        '''Initialize the battery's attributes.'''
        self.battery_size = battery_size


    def describe_battery(self):
        '''Print a statement describing the battery size.'''
        print(f"This car has a {self.battery_size}-kWh battery.")


    def get_range(self):
        '''Print a statement about the range this battery provides.'''
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")


    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100
            print(f"Upgraded Tesla's battery range to {self.battery_size}")
        else:
            print("The battery is already upgraded.")


class ElectricCar(Car):
    '''Represent aspects of a car, specific to electric vehicles.'''
    def __init__(self, make, model, year):
        '''
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        '''
        super().__init__(make, model, year)
        self.battery = Battery()
    #     self.battery_size = 75


    # def describe_battery(self):
    #     '''Print a statement describing the battery size.'''
    #     print(f"This car has a {self.battery_size}-kWh battery.")


    # Showing method overriding.
    def fill_gas_tank(self):
        '''Electric cars don't have gas tanks.'''
        print("This car doesn't have a gas tank!")

my_tesla = ElectricCar("tesla", "model s", 2019)
print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()

old_car = Car('toyota', 'camery', 2014)
old_car.fill_gas_tank()
my_tesla.fill_gas_tank()

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print("\n") 
new_tesla = ElectricCar('tesla', "model x", 2020)
print("\n") 

print(new_tesla.get_descriptive_name())

new_tesla.battery.describe_battery()
new_tesla.battery.get_range()

new_tesla.battery.upgrade_battery()

new_tesla.battery.describe_battery()
new_tesla.battery.get_range()