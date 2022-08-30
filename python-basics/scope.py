# Local scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()


# Global scope

player_health = 20

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
print(player_health)


# There is no block scope

game_level = 3
enemies = ["skeleton", "zombie", "alien"]
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)


# Modifying Global Scope - better to avoid modifying global scope within a function which has local scope

enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


# Global Constants

PI = 3.14159
URL = "https://www.google.com"


