import unittest

from Code.my_calculations import Calculations


class TestCalculations(unittest.TestCase):

	def test_sum(self):
		calculation = Calculations(8,2)
		self.assertEqual(calculation.get_sum(), 10, 'The sum is wrong')
		
if __name__== '__main__':
	unittest.main()
