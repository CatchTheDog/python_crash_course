import json

filename = '..\\test_files\\numbers.json'
with open(filename) as file_object:
	numbers = json.load(file_object)


print(numbers)