enemis = 1
"""def increase_enemies():
    enemis += 1  #local scope
    print(f"number of enemies: {enemis}")

increase_enemies()
print(f"enemies ouside function:{enemis}")"""

#Modifying global scope with local scope

"""def increase_enemies():
    global enemis
    enemis += 2 #local scope
    print(f"number of enemies: {enemis}")

increase_enemies()
print(f"enemies ouside function:{enemis}")"""
#but it is advised to avoid modifying global scope

#instead modigying we use return statement
def increase_enemies():
    print(f"enemies inside function: {enemis}")
    return enemis +2
enemis = increase_enemies() #if we just declare the function without reaasigning into the sem variable then it will show the old value
print(f"enemies oustide function: {enemis}")

