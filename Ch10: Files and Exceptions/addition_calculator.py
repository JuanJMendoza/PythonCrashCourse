'''
Example 10.6: Write a program that prompts for two numbers. Add them together and print the result. Catch the ValueError if either input value is not a number, and print a friendly error message.
Test your program by entering two numbers and then by entering some text instead of a number.

Example 10.7: Wrap your code from Exercise 10.6 in a while loop so the user can continue entering numbers even if they make a mistake and enter text instead of a number.
'''
def add():
    while True:
        print("Press 'q' to quit.")
        val1 = input("\nFirst number: ")
        if val1 == 'q':
            print("You pressed 'q' to quit.")
            break
        val2 = input("Second number: ")
        if val2 == 'q':
            print("You pressed 'q' to quit.")
            break
        try:
            print(f"{int(val1)} + {int(val2)} = {int(val1) + int(val2)}")
        except ValueError:
            print("One of your values is not a number.\n")

add()