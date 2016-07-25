import unittest
from add import add
class test_add(unittest.TestCase):
    def test1(self):
        self.assertEqual(add('"ABCD","DEF","C"'),61)
        self.assertEqual(add('"CDEF","ABC","FIJK"'),150)
        self.assertEqual(add('"AAA","BBB"'),15)

if __name__ == '__main__':
    unittest.main()
