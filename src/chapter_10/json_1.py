import json

numbers = [2,3,5,7,11,13]

filename = '..\\test_files\\numbers.json'
with open(filename,'a') as file_object:
	json.dump(numbers,file_object)