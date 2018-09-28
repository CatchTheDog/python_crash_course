#使用不定长位置形参时，必须要将不定长形参放在最后，且实参要位置对应传入调用
def make_pizza(name,*toppings):
	"""打印顾客点的所有配料"""
	print(name+":"+str(toppings))

make_pizza('pepperoni',"liming")
make_pizza('mushrooms','green peppers','extra cheese','Dany')
