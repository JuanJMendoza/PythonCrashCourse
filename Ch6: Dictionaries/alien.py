alien_0 = {'color': 'green', 'points': 5}

# print(alien_0['color'])
# print(alien_0['points'])

new_points = alien_0['points']
print(f"You just scored {new_points} points!\n")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0, "\n")

print(f"The alien's color is {alien_0['color']}\n")

alien_0['color'] = 'yellow'
print(f"The alien's color is now {alien_0['color']}\n")

alien_0['speed'] = 'medium'

print(f"Original position: {alien_0['x_position']}\n")

# Move the alien to the right.
# Determine how far to move the alien based on it current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}\n")

'''
The del key word tells python to delete the key and associated value with it in 
the example below. The rest of the pairs are unaffected.
'''
print(alien_0)
del alien_0['points']
print(alien_0)
