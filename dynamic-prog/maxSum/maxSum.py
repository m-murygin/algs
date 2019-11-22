#!/usr/bin/python3


def maxSubsetSum(arr):
    max_sums = []
    max_sums.append(arr[0])

    if len(arr) > 1:
        max_sums.append(max(arr[0], arr[1]))

    for i in range(2, len(arr)):
        max_sum = max(max_sums[i - 1], max_sums[i - 2] + arr[i])
        max_sums.append(max_sum)

    return max_sums[-1]


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    print(res)
