'''The asterisk in the parameter name *toppings tells Python to make an empty tuple
 called toppings and pack whatever values it recieves into this tuple.'''

def make_pizza1(*toppings):
    '''Print the list of toppings that have been requested.'''
    print(toppings)

# make_pizza1('pepperoni')

# make_pizza1('mushrooms', 'green peppers', 'extra cheese')

''' ---------------------------------------'''

def make_pizza2(*toppings):
    '''Summarize the pizza we are about to make.'''
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

# make_pizza2('pepperoni')

# make_pizza2('mushrooms', 'green peppers', 'extra cheese')

''' ---------------------------------------'''

def make_pizza3(size, *toppings):
    '''Summarize the pizza we are about to make.'''
    print(f"\nMaking an {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

# make_pizza3(12, 'pepperoni')

# make_pizza3(15, 'mushrooms', 'green peppers', 'extra cheese')