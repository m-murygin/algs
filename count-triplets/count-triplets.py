#!/usr/bin/python3


def get_indexes_map(arr):
    indexes_map = {}
    for i in range(len(arr)):
        if arr[i] not in indexes_map:
            indexes_map[arr[i]] = []

        indexes_map[arr[i]].append(i)

    return indexes_map


def countTriplets(arr, r):
    indexes_map = get_indexes_map(arr)
    print(indexes_map)
    triplets = 0
    for i, el in enumerate(arr):
        next_el = el * r
        next_next_el = next_el * r

        if next_el not in indexes_map or next_next_el not in indexes_map:
            continue

        for j in range(i + 1, len(indexes_map[next_el])):
            for k in range(j + 1, len(indexes_map[next_next_el])):
                triplets += 1

    return triplets


if __name__ == '__main__':
    n, r = map(int, input().split())
    arr = list(map(int, input().rstrip().split()))
    ans = countTriplets(arr, r)
    print(ans)
