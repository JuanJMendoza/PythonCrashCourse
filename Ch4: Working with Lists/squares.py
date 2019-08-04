squares = []

for number in range(1, 11):
    squares.append(number**2)

print(squares)

print("\n")
'''
The functions below would also work just as well if our list contained a million items.
'''
print(min(squares))

print("\n")

print(max(squares))

print("\n")

print(sum(squares))

print("\n")


'''
Using list comprehension to build the same list squares.
'''
squares2 = [value**2 for value in range(1,11)]
print(f"This is the same list of squares from above using list comprehension: \n{squares2}")