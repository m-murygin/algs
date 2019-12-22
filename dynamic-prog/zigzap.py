#!/usr/bin/python3

# Given an array A of N positive integers.
# The task is to find the longest Zig-Zag
# subsequence problem such that all elements
# of this are alternating (Ai-1 < Ai > Ai+1).

# Input:
# The first line of input contains an integer
# T denoting the number of test cases.
# Each test case contains an integer N which
# denotes the number of elements in the array A.
# Next line contains space separated n elements in the array A.

# Output:
# Print the length of the longest such subsequence.


def get_longest_sub_sequence(arr):
    totalLongest = 1
    longestDownList = [1]
    longestUpList = [1]

    for i in range(1, len(arr)):
        longestUp = 1
        longestDown = 1
        for j in range(i):
            if arr[j] < arr[i]:
                longestUp = max(longestUp, longestDownList[j] + 1)
            elif arr[j] > arr[i]:
                longestDown = max(longestDown, longestUpList[j] + 1)

        longestUpList.append(longestUp)
        longestDownList.append(longestDown)
        totalLongest = max(totalLongest, longestUp, longestDown)
        print("UP: ", longestUpList)
        print("DOWN: ", longestDownList)
        print("")

    return totalLongest


def main():
    T = int(input())

    for _ in range(T):
        # we don't need element numbers in python
        input()
        arr = list(map(int, input().split()))
        print(get_longest_sub_sequence(arr))


if __name__ == "__main__":
    main()
