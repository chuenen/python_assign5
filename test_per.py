import unittest
from perferct import perfect
class test_per(unittest.TestCase):
    def test1(self):
        self.assertEqual(perfect(6), True)
        self.assertEqual(perfect(8), False)
    def test2(self):
        self.assertEqual(perfect(28), True)
        self.assertEqual(perfect(55), False)

if __name__ == '__main__':
    unittest.main()
