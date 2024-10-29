import unittest
import dibujo

class TestLimites(unittest.TestCase):
    def test_mod_limites(self):
        self.assertEqual(dibujo.mod_limites('1', 1, 16, 1, 16), [1, 8, 1, 8])
        self.assertEqual(dibujo.mod_limites('2', 1, 16, 1, 16), [1, 8, 9, 16])     
        self.assertEqual(dibujo.mod_limites('1', 1, 8, 9, 16), [1, 4, 9, 12])   
        self.assertEqual(dibujo.mod_limites('3', 1, 16, 1, 16), [9, 16, 9, 16])  
        self.assertEqual(dibujo.mod_limites('4', 1, 16, 1, 16), [9, 16, 1, 8])  
    
    def test_evalua(self):
        self.assertTrue(dibujo.evalua(['2','2','2','2','x']))
        self.assertTrue(dibujo.evalua(['2','2','2','2','x']))

if __name__ == '__main__':
    unittest.main()
