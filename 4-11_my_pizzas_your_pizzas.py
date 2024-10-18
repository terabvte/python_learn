pizzas = ["boscaiola", "margherita", "capricciosa"]

for pizza in pizzas:
    print(f"I love {pizza.title()} pizza.")

print("\nI really love pizza!\n")

# 4-11 beginning

friend_pizzas = pizzas[:]

pizzas.append("diavola")
friend_pizzas.append("quattro formaggi")

for pizza in pizzas:
    print(f"My favorite pizzas are {pizza.title()}")
print("\n")
for pizza in friend_pizzas:
    print(f"My friend's favorite pizzas are {pizza.title()}")