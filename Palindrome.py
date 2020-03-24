# How to check if a string is also a palindrome one

def is_palindrome(s: str) -> bool:
    return True if s.lower() == s[::-1].lower() else False


import unittest


class test_Problem8(unittest.TestCase):
    def test1_result(self):
        self.assertTrue(is_palindrome("hannah"))

    def test2_result(self):
        self.assertFalse(is_palindrome("Hannam"))


if __name__ == '__main__':
    unittest.main()
