# You are in charge of the cake for your niece's birthday and have decided the cake will 
# have one candle for each year of her total age. When she blows out the candles, she’ll 
# only be able to blow out the tallest ones. Your task is to find out how many candles she 
# can successfully blow out.

# For example, if your niece is turning 4 years old, and the cake will have 4 candles of height 4, 4, 1, 3, she will be able 
# to blow out 2 candles successfully, since the tallest candles are of height 4 and there are 2 such candles.

# Function Description
# Complete the function birthdayCakeCandles in the editor below. It must return an integer
# representing the number of candles she can blow out birthdayCakeCandles has the following parameter(s):
# ar: an array of integers representing candle heights
# Constraints
    # 1<= n <= 10^5
    # 1<= ar[i] <= 10^7


class Max_Candle:
    @staticmethod
    def max_candle(arr):
        # The algorithm checks if the length is 0
        if len(arr) == 0:
            return False
        # The algorithm checks if the highest value is  greater than 10^7
        elif max(arr) > 10**7:
            return False
        # The algorithm return the number of the gishest value that list contains.
        else:
            return arr.count(max(arr))
        
    
if __name__ == '__main__':
    arr = [1,3,2,5,5]
    Max_Candle.max_candle(arr)
    