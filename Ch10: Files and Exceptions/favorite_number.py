'''
Exercise 10.11: Write a program that prompts for the user's favorite number. Use json.dump() to store this number in a file. 
Write a separate program that reads in this value and prints the message, "I know your favoite number! It's ___."
'''
import json

def ask_for_fav_num():
    filename = "remembered_numbers.json"

    fav_num = int(input("What's your favorite number? "))

    with open(filename, 'w') as f:
        json.dump(fav_num, f)

def tell_fave_num(filename):
    try:
        with open(filename, 'r') as f:
            fav_num = json.load(f)

    except FileNotFoundError:
        ask_for_fav_num()

    else:
        print(f"I know your favoite number! It's {fav_num}.")

filename = "remembered_numbers.json"

tell_fave_num(filename)