# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structure?

def is_unique_chars(s1: str, s2: str) -> bool:
    return False if len(s1) != len(s2) else True if sorted(s1.lower()) == sorted(s2.lower()) else False


import unittest


class test_Problem8(unittest.TestCase):
    def test1_result(self):
        self.assertTrue(is_unique_chars("hannah", "HANNAH"))

    def test2_result(self):
        self.assertFalse(is_unique_chars("Hannam", "ANNA"))


if __name__ == '__main__':
    unittest.main()
