cars = ['audi','bmw','subaru','toyota']
for car in cars:
	if car.lower() == 'bmw':
		print(car.upper())
	else:
		print(car.title())


requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
	print('Hold the anchovies!')