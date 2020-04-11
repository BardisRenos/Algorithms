import unittest
from Staircase import Staircase


class Test_Staircase(unittest.TestCase):

    def test_number_constraints(self):

        self.assertFalse(Staircase.staircase(200))

    
    def test_number_type(self):
        
        self.assertFalse(Staircase.staircase("10"))
        

if __name__ == "__main__":
    unittest.main()