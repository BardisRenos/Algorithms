
arr = [2, 3, 6, 0, 0, -9, -8]


def plus_minus_count(arr):
    count_positive = 0
    count_zero = 0
    count_negative = 0

    for i in arr:
        if i < 0:
            count_negative += 1
        elif i > 0:
            count_positive += 1
        else:
            count_zero += 1

    return count_negative / len(arr), count_positive / len(arr), count_zero / len(arr)


if __name__ == "__main__":
    print(plus_minus_count(arr))
