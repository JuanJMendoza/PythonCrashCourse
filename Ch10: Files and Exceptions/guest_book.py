'''Exercise 10-4: Write a while loop that prompts users for their name. When they enter their name, print a greeting to the screen and add a line recording
their visit in a file called guest_boobk.txt. Make sure each entry appears on a new line in the file.'''

filename = 'guest_book.txt'

with open(filename, 'a') as file_object:
    guest = ''

    while guest != 'no':
        guest = input("Hello, What is your name? ")
        if guest != 'no':
            file_object.write(f"{guest} has registered at the resort.\n")