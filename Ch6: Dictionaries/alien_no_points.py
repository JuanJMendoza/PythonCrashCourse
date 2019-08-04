alien_0 = {'color': 'green', 'x_position': 0, 'y_position': 25} 
'''
For dictionaries, specifically, you can use the get() method to set a default value that
will be returned if the requested key doesn't exist.
'''
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
'''
If there's a chance the key you're asking for might not exist, consider using the 
get() method instead of the square bracket notation.

If you leave out the second argument in the call to get() and the key doesn't exist,
Python will return the value None. The special valuen None means "no value exists."
This is not an error: it's a special value meant to indicate the absence of a value.
'''