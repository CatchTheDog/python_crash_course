prompt = "\nTell me something, and I will repeat it back to you! \n"
prompt += "\nEnter 'quit' to end the program!\n"
message = ""
while message != 'quit':
	message = input(prompt)
	print(message)