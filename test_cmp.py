import unittest
from compare import compare
class test_cmp(unittest.TestCase):
    def test1(self):
        self.assertEqual(compare('2134,3412,6421,8723,9239,1234,2345'), [9239, 8723, 6421])
        self.assertEqual(compare('12345,6666666,99776,567,88888,456789,34'), [6666666, 456789, 99776])
        self.assertEqual(compare('1,3,5,7,9,10,36,8,33,15'), [36, 33, 15])

if __name__ == '__main__':
    unittest.main()
