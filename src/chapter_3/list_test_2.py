cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

sortedCars = sorted(cars,reverse=True)
print(cars)
print(sortedCars)

print(len(sortedCars))

for car in sortedCars:
	print(car)