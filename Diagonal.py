import numpy as np

# The given 2d array
arr = np.array([[10, 12, -3], [1, 20, 30], [100, 220, 30]])


def diagonal_difference(arr):
    # The index from down left corner
    right_index = arr.shape[0] - 1
    
    # The two variable to sum of the two diagonals 
    sum_left = 0
    sum_right = 0

    for index in range(arr.shape[0]):
        # Add numbers from top left to down right of the array
        sum_left += arr[index][index]
        # Add numbers from down left to top right of the array
        sum_right += arr[right_index - index][index]
    
    # Return the absolute value 
    return abs(sum_left - sum_right)


if __name__ == "__main__":
    print(diagonal_difference(arr))
