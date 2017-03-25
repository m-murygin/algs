#!/usr/bin/python

import argparse
from random import randint

parser = argparse.ArgumentParser(
    description='Gets the n-th smallest element in the array')
parser.add_argument('--list', '-l', type=int, nargs='+',
                    help='an integer array to select')
parser.add_argument('--index', '-i', type=int,
                    help='index to select')
args = parser.parse_args()


def select(input_array, index, start_index=None, end_index=None):
    if start_index is None:
        start_index = 0
    if end_index is None:
        end_index = len(input_array) - 1

    if start_index == end_index:
        return input_array[start_index]

    pivot_index = partition(input_array, start_index, end_index)
    if pivot_index == index:
        return input_array[pivot_index]
    elif pivot_index > index:
        end_index = pivot_index - 1
    else:
        start_index = pivot_index + 1

    return select(input_array, index, start_index, end_index)


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
    buf = array[a_index]
    array[a_index] = array[b_index]
    array[b_index] = buf


def main():
    print select(args.list, args.index)


if __name__ == '__main__':
    main()
