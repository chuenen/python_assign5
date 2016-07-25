import unittest
from listcomprehension import sub
class test_listcom(unittest.TestCase):
    def test1(self):
        self.assertEqual(sub(), -55)

if __name__ == '__main__':
    unittest.main()
    
