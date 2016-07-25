import unittest
from compare import compare
class test_cmp(unittest.TestCase):
    def test1(self):        
        self.assertEqual(compare(), [9239, 8723, 6421])

if __name__ == '__main__':
    unittest.main()
