# Consider a staircase of size : 4

#    #
#   ##
#  ###
# ####

# Observe that its base and height are both equal to , and the image is drawn using # symbols and spaces. The last line is not preceded by any spaces.
# Write a program that prints a staircase of size .
# Function Description
# Complete the staircase function in the editor below. It should print a staircase as described above.
# staircase has the following parameter(s):
# n: an integer

# Input Format
# A single integer, n , denoting the size of the staircase.

# Constraints.
# 0 < n =< 100.

# Output Format
# Print a staircase of size  using # symbols and spaces.
# Note: The last line must have  spaces in it.


class Staircase:
    @staticmethod
    def staircase(n):
        res = type(n) == str
        if res == False:
            if 0 < n <= 100:
                # The index is started from 1 until to the given number.
                for i in range(1, n + 1):
                    # The algorithm prints empty spaces (" ") as the given number - 1 (in the first time and -2 the second time and etc.) and the "#" symbol by 1 in the first time, by 2 in the second time and etc.
                    print(" " * int(n - i), "#" * i)
            else:
                return False
        else:
            return False


if __name__ == "__main__":
    Staircase.staircase(5)
