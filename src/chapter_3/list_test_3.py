for value in range(1,5):
	print(value)


numbers = list(range(1,6))
print(numbers)


numbers = list(range(1,12,3))
print(numbers)


squares = []
for value in range(1,11,1):
	squares.append(value ** 2)
print(squares)

#列表解析
squares = [value**2 for value in range(1,11,1)]
print(squares)
