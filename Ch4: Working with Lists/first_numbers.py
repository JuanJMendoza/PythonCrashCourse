'''
Python starts associating from the first value in the pair of given arguments until 
the value of the second arugment - 1
'''
for value in range(1,5):
    print(value)

print("\n")

'''
Python starts associating variable value with values from 0 until the value of 
the given argument - 1.
'''
for value in range(6):
    print(value)

print("\n")

'''
When you wrap list() around a call to the range() function, the output will be a list 
of numbers.
'''
numbers = list(range(6))
print(numbers)

print("\n")

'''
We can also use the range() function to tell Python to skip numbers in a given range.
If you pass a third argument to range(), Python uses that value as a step size when
generating numbers.
'''
print(list(range(0,7,2)))