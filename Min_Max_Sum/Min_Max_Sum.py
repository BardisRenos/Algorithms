
class Min_Max_Sum:
    @staticmethod
    def find_min_max_sum(arr):
        # The algorithm checks if the length is 0.
        if len(arr) == 0:
            return False
        # Here the algorithm checks if the maximum value of the list is greater than 10^9    
        elif max(arr) > 10 ** 9:
            return False
        else:
            sum_res = sum(arr)
            
            return sum_res - max(arr), sum_res - min(arr)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]

    print(Min_Max_Sum.find_min_max_sum(arr))
