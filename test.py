from program import sum_of_n_numbers
import unittest

class Test_Program(unittest.TestCase):
    def test_case_1(self):
        r1 = sum_of_n_numbers(5)
        self.assertEqual(r1, 15)
    def test_case_2(self):
        r2 = sum_of_n_numbers(8)
        self.assertEqual(r2,36)
    def test_case_2(self):
        r3 = sum_of_n_numbers(10)
        self.assertEqual(r3,50)
    def test_case_2(self):
        r4 = sum_of_n_numbers(7)
        self.assertEqual(r4,28)
    def test_case_2(self):
        r5 = sum_of_n_numbers(12)
        self.assertEqual(r5,55)
if __name__ == '__main__':
    unittest.main()