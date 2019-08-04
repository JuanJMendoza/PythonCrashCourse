motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

# motorcycles[0] = "ducati"
# print(motorcycles)

# The append() adds 'ducati' to the end of the list w/o affecting the other elements.
motorcycles.append("ducati")
print(motorcycles)

"""
You can add a new element at any postion using insert(). You do this by specifying
the index of the new element and the value of the new item.
"""
motorcycles.insert(0, "harley")
print(motorcycles)

"""
You can remove an item from any postion in a list using the del statement if you
know its index.
"""
del motorcycles[0]
print("deleted harley from the list:", motorcycles)

del motorcycles[0]
print("deleted honda from the list:", motorcycles)

print("\n")
"""
Sometimes you'll want to use the value of an item after you remove it from a list.
The pop() method removes the last item in a list, but it lets you work with that item 
after removing it.
"""
#Lets pop a motorcycle from the list of motorcycles.
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print("Popped the motorcycle", popped_motorcycle, "from the motorcycle list.")

print("\n")
motorcycles = ["honda", "yamaha", "suzuki"]
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

"""
You can use pop() to remove an item from any position in a list by including
the index of the item you want to remove in the parentheses.
"""
print("\n")
motorcycles = ["honda", "yamaha", "suzuki"]
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I ever owned was a {first_owned.title()}.")

'''
When you want to delete an item from a list and not use that item in any way, use the
del statement; if you want to use an item as you remove it, use the pop() method.
'''

'''
Sometimes you won't know the index of the item you want to delete. If you know the 
value of the item you want to remove, you can use the remove() method.
'''
print("\n")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

motorcycles.remove("honda")
print(motorcycles)

'''
The remove() method only removes the first instance of the item we specify. If there's
a possibility the item appears more than once we'll need to use a loop to make sure
we remove all instances.
'''