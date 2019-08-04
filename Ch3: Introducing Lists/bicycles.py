bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)
print(bicycles[0].title())

# By asking for the item at index -1, Python always returns the last item in the list.
print(bicycles[-1])

"""
This extends to other negative indexes as well. Index -2 returns the 2nd to last 
element in the list and so on and so forth.
"""
print (bicycles[-2].title())

# You can use individual values from a list just as you would any other variable.
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)