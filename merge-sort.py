#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(
    description='Sort array with merge sort algorithm')
parser.add_argument('integers', type=int, nargs='+',
                    help='an integer array to sort')
args = parser.parse_args()


def merge_sort(input_array):
    input_length = len(input_array)
    if input_length < 2:
        return input_array
    else:
        half_length = input_length / 2
        first_half = input_array[:half_length]
        first_sorted = merge_sort(first_half)

        second_half = input_array[half_length:]
        second_sorted = merge_sort(second_half)

        return merge(first_sorted, second_sorted)


def merge(a, b):
    len_a = len(a)
    len_b = len(b)
    res = list()
    pointer_a = 0
    pointer_b = 0

    while True:
        if a[pointer_a] < b[pointer_b]:
            res.append(a[pointer_a])
            pointer_a += 1

            if pointer_a >= len_a:
                res.extend(b[pointer_b:])
                break
        else:
            res.append(b[pointer_b])
            pointer_b += 1

            if pointer_b >= len_b:
                res.extend(a[pointer_a:])
                break

    return res


def main():
    print merge_sort(args.integers)


if __name__ == '__main__':
    main()
