'''
To copy a list, we can make a slice that includes the entire original list by ommiting
the first index and the second index ([:]). This tells Python to make a slice that 
starts at the first item and ends witht the last item, producing a copy of the entire
list.
'''
favorite_foods = ["pizza", "falafel", "carrot cake"]
friend_fav_food = favorite_foods[:]

print("My favorite foods are: ", "\n", favorite_foods, "\n",)
print("My friend's favorite foods are: ", "\n", friend_fav_food)
print("\n")
'''
To prove that we have two seperate lists, we'll add a new food to each list and show
that each list keeps track of the appropriate person's favorite foods.
'''
favorite_foods.append("lasagna")
friend_fav_food.append("zuccini")
print("My favorite foods are: ", "\n", favorite_foods, "\n",)
print("My friend's favorite foods are: ", "\n", friend_fav_food)
print("\n")
'''
If we had simply set 
friend_fav_foods = favorite_foods, 
we would not produce two seperate lists.
For example, here's what happens when you try to copy a list without using a slice:
'''
#This doesn't work:
my_foods = ["pizza", "falafel", "carrot cake"]

friends_food = my_foods
my_foods.append("banana")
friends_food.append("apple")
print("My fav. foods are:")
print(my_foods)
print("\n")
print("My friend's fav. foods are:")
print(friends_food)
print("\n")
'''
This sytax actually tells Python to associate the new variable friend_foods with the 
list that is already associated with my_foods, so now both variables point to the same
list.
MAKE SURE YOU'RE COPYING A LIST USING A SLICE IF YOU WANT A SEPERATE LIST WITH THE
SAME ELEMENTS AS THE LIST BEING COPIED.
'''