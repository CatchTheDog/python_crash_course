car = 'subaru'
print("Is car == 'subaru'? I predict True!")
print(car == 'subaru')


requested_toppings = []
if requested_toppings:
	for requested_topping in requested_toppings:
		print("Adding "+ requested_topping)
	print("\n\tFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza?")