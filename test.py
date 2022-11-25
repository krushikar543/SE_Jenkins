from program import Fibonacci
import unittest

class Test_Program(unittest.TestCase):
    def test_case_1(self):
        r1 = Fibonacci(3)
        self.assertEqual(r1, 2)
    def test_case_2(self):
        r2 = Fibonacci(5)
        self.assertEqual(r2,5)
    def test_case_3(self):
        r3 = Fibonacci(7)
        self.assertEqual(r3,12)
    def test_case_4(self):
        r4 = Fibonacci(10)
        self.assertEqual(r4,55)
    def test_case_5(self):
        r5 = Fibonacci(12)
        self.assertEqual(r5,145)
if __name__ == '__main__':
    unittest.main()
