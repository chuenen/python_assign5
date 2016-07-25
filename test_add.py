import unittest
from add import add
class test_add(unittest.TestCase):
    def test1(self):
        self.assertEqual(add(),96)

if __name__ == '__main__':
    unittest.main()        
