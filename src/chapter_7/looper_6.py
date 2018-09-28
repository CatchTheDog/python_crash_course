prompt = "\nTell me something, and I will repeat it back to you! \n"
prompt += "\n(Enter 'quit' to end the program!)\n"
message = ""
while True:
	city = input(prompt)
	if city == 'quit':
		break
	else:
		print("I'd love to go to "+ city.title()+"!")