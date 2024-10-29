import unittest
import calcula

class TestCalcula(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(calcula.suma(10, 5), 15)
        self.assertEqual(calcula.suma(20, 5), 25)

    def test_resta(self):
        self.assertEqual(calcula.resta(10, 5), 5)
        self.assertEqual(calcula.resta(20, 5), 15)

    def test_multi(self):
        self.assertEqual(calcula.multi(10, 5), 50)
        self.assertEqual(calcula.multi(20, 5), 100)
        
if __name__ == '__main__':
    unittest.main()
