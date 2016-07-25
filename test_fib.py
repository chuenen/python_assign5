import unittest
from fibonacci import fib
class test_fib(unittest.TestCase):
    def test1(self):
        f = fib()
        self.assertEqual(f.next(), 1)
        self.assertEqual(f.next(), 2)
        self.assertEqual(f.next(), 3)
        self.assertEqual(f.next(), 5)
        self.assertEqual(f.next(), 8)
    def test2(self):
        f = fib()
        self.assertEqual(f.next(), 1)
        self.assertEqual(f.next(), 2)
        self.assertEqual(f.next(), 3)
        self.assertEqual(f.next(), 5)
        self.assertEqual(f.next(), 8)

if __name__ == '__main__':
    unittest.main()
