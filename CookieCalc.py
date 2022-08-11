
numCookies = int(input("How many cookies would you like?: "))

print(f"\nFor {numCookies} cookies, you will use:")

Butter = 1/16 * numCookies
Sugar = (1/2)/16 * numCookies
Flour = 2/16 * numCookies

print(f"{Butter} C butter")
print(f"{Sugar} C sugar")
print(f"{Flour} C flour")

numEat = int(input("\n\nMore importantly, how many will you be eating?: "))
Calories = 160 * numEat 
Carbs = 18 * numEat
Fat = 12 * numEat

print(f"{numEat} cookie(s) will provide {Calories} calories, {Fat}g fat, and {Carbs}g\ncarbohydrate. Enjoy!!")
