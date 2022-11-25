from program import sum_of_n_numbers
import unittest

class Test_Program(unittest.TestCase):
    def test_case_1(self):
        r1 = sum_of_n_numbers(1)
        self.assertEqual(r1, 1)
    def test_case_2(self):
        r2 = sum_of_n_numbers(15)
        self.assertEqual(r2,120)
   
if __name__ == '__main__':
    unittest.main()