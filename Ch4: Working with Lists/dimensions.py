'''
A tuple looks like a list except it has parentheses instead of square brackets.
Once you define a tuple, you can access individual elements by using each item's index, 
just as you would for a list. Tuples are immutable, so once you put an element in one
you cannot change it.
'''
rectangle = (200, 50)
print(rectangle[0])
print(rectangle[1])
print(rectangle)
'''The line below gives a TypeError: 'tuple object does not support item assignment'''
#rectangle[0] = 250

'''
Tuples are technically defined by the presence of a comma; the parentheses make them
look neater and more readable. If you want to define a tuple with one element, you need
to include the trailing comma.
'''
my_t = (3,)
print(my_t)
print(my_t[0])
'''
You can loop over all the elements in a tuple just like you can with a list
'''
print("loop below")
for dim in rectangle:
    print(dim)

'''
Although we can't modify a tuple, you can assign a new value to a variable that 
represents a tuple. So if we wanted to change our dimensions, we could redefine 
the entire tuple:
'''
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

'''Python doesn't raise any values this time because reassigning a variable is valied'''
'''
Use tuples when you want to store a set of values that should not be changed throughout
the life of a program.
'''