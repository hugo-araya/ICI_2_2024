import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_es_primo(self):
        self.assertFalse(utils.es_primo(4))
        self.assertTrue(utils.es_primo(2))
        self.assertTrue(utils.es_primo(3))
        self.assertFalse(utils.es_primo(8))
        self.assertFalse(utils.es_primo(10))
        self.assertTrue(utils.es_primo(7))
        self.assertEqual(utils.es_primo(-3), "Los números negativos no están permitidos")

if __name__ == '__main__':
    unittest.main()