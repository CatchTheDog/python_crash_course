#位置实参与关键字实参
#函数参数默认值

def describe_pet(pet_name,animal_type='dog'):
	"""显示宠物的信息"""
	print("\nI have a "+ animal_type+".")
	print("My "+animal_type+"'s name is "+pet_name+".")

describe_pet("hamster",'harry')

describe_pet(pet_name='harry',animal_type='hamster')

describe_pet('wangwang')
