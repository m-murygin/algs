#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(
    description='Sort array with merge sort algorithm')
parser.add_argument('integers', type=int, nargs='+',
                    help='an integer array to sort')
args = parser.parse_args()


def quick_osrt(input_array):
    new_pivot = partition(input_array, 0)

    return input_array


def partition(array, pivot_index):
    if pivot_index != 0:
        swap(array, 0, pivot_index)

    pivot_value = array[0]

    new_pivot = 0
    for i in xrange(1, len(array)):
        if pivot_value > array[i]:
            new_pivot += 1
            swap(array, i, new_pivot)

    swap(array, 0, new_pivot)
    return new_pivot

def swap(array, a_index, b_index):
    a = array[a_index]
    array[a_index] = array[b_index]
    array[b_index] = a


def main():
    print quick_osrt(args.integers)


if __name__ == '__main__':
    main()
