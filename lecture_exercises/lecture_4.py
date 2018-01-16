import unittest
#basic unittest framework syntax

class TestMyCode(unittest.TestCase):
	#every test needs to start with literal "test"
	def test_my_first_function(self):
		pass
	def testSomething(self):
		pass

	#inside test functions we should use the assert method to express conditions 
	#your code should meet

#fail() statement will fail upon reaching
#add unittest.main() to actually run the previously defined tests
unittest.main()

#python try/ except blocks
try:
	print("try")
	self.fail()
except
	print("except")

#self.assertRaises(ValueError, best_two_keys, dict2)
