#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(
    description='Count the number of inversions inside array')
parser.add_argument('--array', type=int, nargs='+',
                    help='an integer array to count')
parser.add_argument('--file', type=str,
                    help='file to read integer array (one number on in line)')
args = parser.parse_args()


def count_inversions(arr):
    arr_length = len(arr)
    if arr_length == 1:
        return 0
    else:
        half_length = arr_length / 2
        first_half = arr[:half_length]
        first_inversions = count_inversions(first_half)

        second_half = arr[half_length:]
        second_inversions = count_inversions(second_half)

        split_inversions = sort_and_count_split_inversions(
            arr, first_half, second_half)

        return first_inversions + second_inversions + split_inversions


# assume that first half and second half are sorted inside each other
def sort_and_count_split_inversions(arr, first_half, second_half):
    first_len = len(first_half)
    second_len = len(second_half)

    first_pointer = 0
    second_pointer = 0
    inversions = 0
    for i in xrange(0, len(arr)):
        if first_pointer == first_len:
            arr[i] = second_half[second_pointer]
            second_pointer += 1
        elif second_pointer == second_len or \
                first_half[first_pointer] <= second_half[second_pointer]:
            arr[i] = first_half[first_pointer]
            first_pointer += 1
        else:
            arr[i] = second_half[second_pointer]
            inversions += first_len - first_pointer
            second_pointer += 1

    return inversions


def main():
    if args.array:
        print count_inversions(args.array)
    elif args.file:
        file_name = args.file
        with open(file_name) as f:
            content = f.readlines()
        array = [int(x) for x in content]
        print count_inversions(array)


if __name__ == '__main__':
    main()
