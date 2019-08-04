'''
Make a list of the numbers from one to one million, and then use the min() and max() to
make sure your list actually starts at one and ends at one million. Also, use the sum()
function to see how quickly Python can add one million numbers.
'''
one_million = list(range(1,1_000_001))
print("The smallest number in the list is:", min(one_million))
print("The largest number in the list is:", max(one_million))
print("The sum of all the numbers in the list is:", sum(one_million))
