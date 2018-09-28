class Dog():
	"""一次模拟小狗的简单尝试"""
	
	
	def __init__(self,name,age):
		"""初始化属性name和age"""
		self.name = name
		self.age = age
		self.hobby = 'eat'
	
	
	def sit(self):
		""" 模拟小狗被命令蹲下"""
		print(self.name.title()+"is now sitting!")
	
	
	def roll_over(self):
		"""模拟小狗被命令时打滚"""
		print(self.name.title()+"rolled over!")

	def self_introduce(self):
		"""模拟自我介绍"""
		print("Hello,I'm "+self.name+",my hobby is "+self.hobby)

my_dog = Dog('willie',6)
print("My dog's name is "+my_dog.name.title()+".")
print("My dog's is "+str(my_dog.age)+"years old.")
my_dog.sit()
my_dog.roll_over()
my_dog.self_introduce()