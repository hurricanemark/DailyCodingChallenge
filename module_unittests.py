import unittest
import codechallenge_001

class TestCodeChallenge(unittest.TestCase):

	def codeChallenge_01_test(self):
		nums = [4,20,15,3,72,2,7,90,8,7,9,10,22]
		k = 28
		result = codechallenge-01.isSumOfK(nums,k)
		self.assertEqual(result, True)

if __name__ == '__main__':
	unittest.main()
