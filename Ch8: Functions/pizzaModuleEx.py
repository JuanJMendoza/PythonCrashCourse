'''Practicing importing a module'''

# import pizza 
# pizza.make_pizza3(13, 'pepperoni', 'mushrooms', 'spinach')

print("-----------------------------------------------------------")

# from pizza import make_pizza2 as mp2 

# mp2('chicken', 'extra cheese')

# import pizza as p 

# p.make_pizza1('extra cheese', 'sausage')

from pizza import *

make_pizza3(11, 'mushrooms', 'extra cheese')

make_pizza2('mushrooms', 'extra cheese')

make_pizza1('mushrooms', 'extra cheese')
