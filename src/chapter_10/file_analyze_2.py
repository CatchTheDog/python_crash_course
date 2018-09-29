def count_words(filename):
	"""计算一个文件大致包含多少个单词"""
	try:
		with open(filename) as file_object:
			contents = file_object.read()
	except FileNotFoundError:
		# 获取异常后，忽略异常
		pass
	else:
		# 计算文件大致包含多少个单词
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + " words .")

