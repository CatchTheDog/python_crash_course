from name_function import get_formatted_name as formatted

print("Enter 'q' at any time to quit. ")
while True:
	first = input("\nPlease give me a first name:")
	if first == 'q':
		break;
	last = input("\nPlease give me a last name:")
	if last == 'q':
		break;
	
	formatted_name = formatted(first,last)
	print("\nNeatly formatted name:" + formatted_name)