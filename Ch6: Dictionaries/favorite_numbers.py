'''
Use a dictionary to store people's favorite numbers. Think of 5 names, and use them as 
keys in your dictionary. Think of a favorite number for each person, and store each as 
a value in your dictionary. Print each person's name and thier favorite number. For
even more fun, poll a few friends and get some actual data for your program.
'''
poll_fav_nums = {
    'juan': [1,3,5,7,13,93],
    'erika': [4,8,9,95],
    'gerardo': [8],
    'nancy': [],
}
print("Results from \"favorite number poll\"\n".title())
for name, fav_nums in poll_fav_nums.items():
    if(len(fav_nums) == 1):
        print(f"\n{name.title()}\'s favorite number is {fav_nums[0]}!")
    elif(len(fav_nums) == 0 ):
        print(f"\n{name.title()} doesn't have any favorite numbers!")
    else:
        print(f"\n{name.title()}\'s favorite numbers are: ", end = "")
        for num in fav_nums:
            print(f"{num}", end=" ")
        print("\n")

'''
A set is a collection in which each item MUST BE UNIQUE.
'''
# Old code from previous exercise which cant be ran anymroe because of change in 
# dictionary format.
# for num in set(poll_fav_nums.values()):
#     print(num)
