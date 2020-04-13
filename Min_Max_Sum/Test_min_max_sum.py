import unittest
from Min_Max_Sum import Min_Max_Sum

class Test_Min_Max_Sum(unittest.TestCase):

    def test_array_length(self):
        test_list = []
        self.assertFalse(Min_Max_Sum.find_min_max_sum(test_list))
    
    def test_max_number_size(self):
        test_list2 = [1,2, 10**85]
        self.assertFalse(Min_Max_Sum.find_min_max_sum(test_list2))

    def test_result(self):
        list_res = (10, 14)
        arr = [1, 2, 3, 4, 5]
        self.assertTupleEqual(Min_Max_Sum.find_min_max_sum(arr), list_res)

if __name__ == '__main__':
    unittest.main()