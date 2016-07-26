import unittest
from listcomprehension import sub
class test_listcom(unittest.TestCase):
    def test1(self):
        self.assertEqual(sub(1, 10), -55)
        self.assertEqual(sub(1, 100), -5050)

if __name__ == '__main__':
    unittest.main()
