available_toppings = ["mushrooms", "green peppers", "olives", "pineapple", "pepperoni",
                        "extra cheese"]
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
'''
When the name of a list is used in an if statement, Python returns True if it has 
at least one item in it, otherwise it return False.
''' 
# requested_toppings = []
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry, we don't have {requested_topping}.")        

print("\nFinished making your pizza!")