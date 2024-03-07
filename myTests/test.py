import unittest

from Code.my_calculations import Calculations


class TestCalculations(unittest.TestCase):

	def test_sum(self):
		calculation = Calculations(8,2)
		self.assertEqual(calculation.get_sum(), 10, 'The sum is wrong')
		
	def test_difference(self):
		calculation = Calculations(8,2)
		self.assertEqual(calculation.get_difference(), 6, 'The difference is wrong')
		
	def test_product(self):
		calculation = Calculations(8,2)
		self.assertEqual(calculation.get_product(), 16, 'The product is wrong')
		
	def test_quotient(self):
		calculation = Calculations(8,2)
		self.assertEqual(calculation.get_quotient(), 4, 'The sum is wrong')
		
if __name__== '__main__':
	unittest.main()
