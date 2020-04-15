import unittest
from Candle import Max_Candle

class Test_Max_Cadle(unittest.TestCase):
    
    def test_result(self):
        arr = [1, 2, 4, 4]
        self.assertEqual(Max_Candle.max_candle(arr), 2)
        
    def test_length(self):
        arr = []
        self.assertFalse(Max_Candle.max_candle(arr)) 
    
    def test_element_lenght(self):
        arr = [1, 2, 10**22]
        self.assertFalse(Max_Candle.max_candle(arr))
        

if __name__ == '__main__':
    unittest.main()
    