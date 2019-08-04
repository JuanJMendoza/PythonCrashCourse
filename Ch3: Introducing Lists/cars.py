'''
Imagine we have a list of cars and want to change the order of the list to store them
alphabetically. To keep the task simple, let's assume that all the values in the
list are lowercase.
'''
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print("\n")

#The sort() method changes the order of the list PERMANENTLY.
cars.sort()
print(cars)
print("\n")

'''
You can also sort this list in reverse alphabetical order by passing the argument 
reverse = true to the sort() method.
'''
cars.sort(reverse = True)
print(cars)
print("\n")

'''
To maintain the original order of a list but present it in a sorted order, you can
use the sorted() function. The sorted() function lets you present the list in a certain
order but doesn't affect the actual order of the list.
'''
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here's the original list\n",cars)
print("Here's the temporarily ordered list\n", sorted(cars))
print("Here's the unaffected original list\n",cars)
print("\n")

'''
The sorted() function can also accept a reverse = True argument if we want to display
a list in reverse alphabetial order.
'''

'''
To reverse the original order of a list, we can use the reverse() method. The reverse()
method changes the order of a list PERMANENTLY, but you can revert to the original order
anytime by applying reverse() to the same list a second time.
'''

#Use the length() function to find the length of a list.
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))