file_name = "..\\test_files\\pi_digits.txt"

with open(file_name) as file_object:
	lines_1 = file_object.readlines()

for line in lines_1:
	print(line.rstrip())