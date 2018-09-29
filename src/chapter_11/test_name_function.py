import unittest
from name_function import get_formatted_name as formatted

class NamesTestCase(unittest.TestCase):
	"""测试name_function.py"""
	
	def test_first_last_name(self):
		"""能够正确地处理Janis Joplin这样的姓名吗？"""
		formatted_name = formatted('janis','joplin')
		self.assertEqual(formatted_name,'Janis Joplin')

#unittest.main() 无效，需要使用如下两种方式
# unittest.main

if __name__ == '__main__':
	unittest
