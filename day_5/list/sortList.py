foodMenu = ["cake", "icecream", "Chocolate", "Chips","pancake", "nuggets", "applepie"]

candy = ["milkybar", "Cadbury", "mangobar", "galaxy"]
print(foodMenu)

foodMenu.sort()
print(foodMenu)

foodMenu.sort(reverse = True)
print(foodMenu)


foodMenu.sort(key = str.lower)
print(foodMenu)



foodMenu.extend(candy)
print(foodMenu)