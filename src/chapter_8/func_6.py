def make_pizza(size,*toppings):
	"""概述要制作的披萨"""
	print("\nMaking a"+str(size)+"-inch pizza with the flowing toppings:\n")
	for topping in toppings:
		print("-"+topping)
		
		
def say_hello(name):
	print("Hello,"+name)


def say_bye(name):
	print("Bye,"+name)