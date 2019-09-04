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


class Privilages:
    def __init__(self, first_name, last_name, privilages=[]):
        self.privilages = privilages
        self.first_name = first_name
        self.last_name = last_name

    def show_privilages(self):
        privilages = ", ".join(self.privilages[:-1])
        print(f"The admin, {self.first_name.title()} {self.last_name.title()}, has the following privilages: They {privilages}, and {self.privilages[-1]}.")


class Admin(User):
    def __init__(self, first_name, last_name, age, hometown ):
        super().__init__(first_name, last_name, age, hometown)

        self.privilages = Privilages(first_name, last_name)
    

# new_admin = Admin("jack", "black", 50, "Los Angelas, CA", ["can add posts", "can delete posts", "can ban users"])

# new_admin.show_privilages()

new_new_admin = Admin("brad", "pitt", 50, "los angelas, CA")
new_new_admin.privilages.privilages = ["can add posts", "can delete posts", "can ban users"]
new_new_admin.privilages.show_privilages()