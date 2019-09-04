class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        print(f"The Restaurant {self.restaurant_name} is known for its {self.cuisine_type} cuisine.")


    def open_restaurant(self):
        print(f"{self.restaurant_name} is Open!")


    def set_number(self, number_served):
        self.number_served = number_served


    def increment_number_served(self, number_served):
        if number_served >= 0:
            self.number_served += number_served
        else:
            self.number_served += 0


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors=[]):
        super().__init__(restaurant_name, cuisine_type)

        self.flavors = flavors


    def display_flavors(self):
        flavors = ", ".join(self.flavors[:-1])
        print(flavors + ", and " + self.flavors[-1])

i_scream_for_ice_cream = IceCreamStand("I Scream For Ice Cream", "Ice Cream", ["vanilla", "chocolate", "cookies n' cream", "strawberry"])
i_scream_for_ice_cream.display_flavors()
