pizza_toppings = "\nHello, what kind of pizza toppings would you like? "
pizza_toppings += "\nWhen you're finished adding toppings type 'quit'. "

active = True
total_toppings = []

while active:

    toppings = input(pizza_toppings).title() 

    if toppings.lower() == 'quit':

        active = False
        thank_you = "Thank you, we've added "

        for topping in range(0, len(total_toppings)):

            if(len(total_toppings)>1):

                if(topping == len(total_toppings)-1):

                    thank_you += "and " + total_toppings[topping]
                    print(thank_you,"to your pizza.")

                else:

                    thank_you += total_toppings[topping] + ", "

            else:

                print(thank_you,total_toppings[topping],"to your pizza.")

    else:

        if not (toppings in total_toppings):

            total_toppings.append(toppings)

        print(f"Added {toppings} to your pizza.")
