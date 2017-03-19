#!/usr/bin/python

import argparse
from random import randint

parser = argparse.ArgumentParser(
    description='Sort array with merge sort algorithm')
parser.add_argument('integers', type=int, nargs='+',
                    help='an integer array to sort')
args = parser.parse_args()


def quick_sort(input_array, start_index=None, end_index=None):
    if start_index is None:
        start_index = 0
    if end_index is None:
        end_index = len(input_array) - 1

    if end_index - start_index < 1:
        return

    pivot_index = partition(input_array, start_index, end_index)
    quick_sort(input_array, start_index, pivot_index -1)
    quick_sort(input_array, pivot_index + 1, end_index)

    return input_array


def partition(array, start_index, end_index):
    pivot_index = randint(start_index, end_index)
    swap(array, start_index, pivot_index)

    pivot_value = array[start_index]
    new_pivot = start_index

    for i in xrange(start_index + 1, end_index + 1):
        if pivot_value > array[i]:
            new_pivot += 1
            swap(array, i, new_pivot)

    swap(array, start_index, new_pivot)
    return new_pivot

def swap(array, a_index, b_index):
    a = array[a_index]
    array[a_index] = array[b_index]
    array[b_index] = a


def main():
    print quick_sort(args.integers)


if __name__ == '__main__':
    main()
