'''
To output the first three elements in a list, you would request indicies 0 through 3,
which would return elements 0, 1, and 2.
'''
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("\n")
print(f"The original list is: {players}")
print("\n")
print(players[0:3])
'''
You can generate any subset of a list. For example, if you want the second, third, and
fourth items in a list, you would start the slice from index 1 and end at index 4. 
(Just like range(), the second argument is noninclusive.)
'''
print(players[1:4])
'''
If you omit the first index in a slice, Python automatically starts your slice at the
beginning of the list.
'''
print(players[:4])
'''
A similar syntax works if you want a slice that includes the end of the list.
For example, if you want all the items from the third item through the last item,
you can start with index 2 and omit the second index.
'''
print(players[2:])
'''
Recall that a negative index returns an element a certain distance from the end of the
list; therefore, you can output any slice from the end of a list. For example, if we
want to output the last three players on the roster, we can use the slice players[-3:]
'''
print(players[-3:])
''' Adding a third value in the splice notation would skip every third
argument's value in the list. For example, below it begins to print from the 0th index
then skips the subsequent one, prints index 2 and skips the subsequent one.'''
print(players[0::2])

print("\n")
'''
In the next example we loop through the first three players and print their names
as part of a simple roster.
'''
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player)