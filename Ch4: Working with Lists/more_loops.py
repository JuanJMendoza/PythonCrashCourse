'''
Choose a version of foods.py, and write two for loops to print each list of foods.
'''
favorite_foods = ["pizza", "falafel", "carrot cake"]
friend_fav_food = favorite_foods[:]
favorite_foods.append("lasagna")
friend_fav_food.append("salad")
for food in favorite_foods:
    print(food)
print("\n")
for food in friend_fav_food:
    print(food)