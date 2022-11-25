from program import fibonacci
import unittest

class Test_Program(unittest.TestCase):
    def test_case_1(self):
        r1 = fibonacci(4)
        self.assertEqual(r1, 3)
    def test_case_2(self):
        r2 = fibonacci(7)
        self.assertEqual(r2,21)
   
if __name__ == '__main__':
    unittest.main()
