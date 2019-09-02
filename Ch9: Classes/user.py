'''Make a class called User. Create two attributes called first_name and last_name, and
   then create several other attributes that are typically stored in a user profile.
   Make a method called describe_user() that prints a summary of the user's information.
   Make another method called greet_user() that prints a personalized greeting to the 
   user.
   Create several instances representing different users, and call both methods for 
   each user.'''

class User:
    def __init__(self, first_name, last_name, age, hometown):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hometown = hometown
        self.login_attempts = 0

    def describe_user(self):
        print(f"""{self.first_name} {self.last_name} is {self.age} years old and is from {self.hometown}.""")
    

    def greet_user(self):
        print(f"Hello, {self.first_name}, it's a pleasure to meet you.")


    def increment_login_attempts(self):
        self.login_attempts += 1


    def reset_login_attempts(self):
        self.login_attempts = 0            


me = User("Juan", "M****", "26", "Brooklyn, New York")
me.describe_user()
me.greet_user()

print("\n")

erika = User("Erika", "Z****", "24", "Cuenca, Ecuador")
erika.describe_user()
erika.greet_user()

print("\n")

me.increment_login_attempts()
print(f"{me.first_name}, you have {me.login_attempts} login attempts.")

me.increment_login_attempts()
print(f"{me.first_name}, you have {me.login_attempts} login attempts.")

me.reset_login_attempts()
print(f"{me.first_name}, you have {me.login_attempts} login attempts.")
