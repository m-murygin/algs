#!/usr/bin/python3


def getLongestIncreaing(arr, n):
    totalLongest = 1
    longestList = [1]
    for i in range(1, n):
        longest = 1
        for j in range(i):
            if arr[i] > arr[j]:
                longest = max(longest, longestList[j] + 1)

        longestList.append(longest)
        totalLongest = max(totalLongest, longest)

    return totalLongest


def main():
    T = int(input())

    for _ in range(T):
        n = int(input())
        arr = list(map(int, input().split()))
        print(getLongestIncreaing(arr, n))


if __name__ == "__main__":
    main()
