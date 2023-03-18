
pizzas = ['Pepperoni', 'Fajita', 'Tex Mex']

friend_pizzas = pizzas[:]
pizzas.append('Creamy tikka')
friend_pizzas.append('Bar b q')

print("My pizzas are:")
for pizza in pizzas:
    print("- " + pizza)

print("\nMy friend's pizzas are:")
for pizza in friend_pizzas:
    print("- " + pizza)
