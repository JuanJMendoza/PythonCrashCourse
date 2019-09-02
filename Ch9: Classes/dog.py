''' By convention, capitalized names refer to classes in Python.
    There are no parentheses in the class definition because we're vreating this class from
    scratch. '''
class Dog:
    """A simple attempt to model a dog."""

    # A function that's part of a class is a method.
    def __init__(self,name, age):
        """Initialize name and age attributes"""

        ''' Any variable prefixed with self is available to every method in the class.
            and we'll also be able to access these variables through any instance 
            created from the class.'''
        # Variables set like this are called arributes.
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")

my_dog = Dog("Willie", 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

your_dog = Dog("Lucy", 3)

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()