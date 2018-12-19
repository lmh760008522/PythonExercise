import unittest

def get_fomatted_name(first, last):
	"""generate a neatly name"""
	full_name = first + ' ' + last
	return full_name.title()

class NameTestCase(unittest.TestCase):
	"""docstring for NameTestCase"""

	def test_first_last_name(self):
		formatted_name = get_fomatted_name('jason', 'jollin')
		self.assertEqual(formatted_name, 'Jason Jollin')
		
	def ():
		pass



unittest.main()