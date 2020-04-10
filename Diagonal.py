import numpy as np

arr = np.array([[10, 12, -3], [1, 20, 30], [100, 220, 30]])


def diagonal_difference(arr):
    right_index = arr.shape[0] - 1

    sum_left = 0
    sum_right = 0

    for index in range(arr.shape[0]):
        sum_left += arr[index][index]
        sum_right += arr[right_index - index][index]

    return abs(sum_left - sum_right)


if __name__ == "__main__":
    print(diagonal_difference(arr))
