import unittest
from app import welcome

class Testing(unittest.TestCase):
    def test_welcome(self):
        self.assertEqual(welcome(), 'Please add /docker after the port 8888')

if __name__ == '__main__':
    unittest.main()