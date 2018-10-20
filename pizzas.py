favorite_pizza = ['sausage', 'cheese', 'bacon']
friend_pizzas = favorite_pizza[:]

favorite_pizza.append('pepperoni')
friend_pizzas.append('chicken')

print('My favorite pizzas are:')
for pizza in favorite_pizza:
	print(pizza)

print("\nMy friend's favorite pizza are:")
for pizza in friend_pizzas:
	print(pizza)
	
