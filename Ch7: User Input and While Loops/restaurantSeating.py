numOfPeople = input("How many guests will you have in your party? ")

numOfPeople = int(numOfPeople)

if (numOfPeople > 8):
    print("Okay, just a moment while we wait for a table to free up.")
else:
    print("Your table is ready.")