#!/usr/bin/python

import argparse
import math

parser = argparse.ArgumentParser(
    description='Count the number of inversions inside array')
parser.add_argument('-l', '--left', type=int, nargs='+', required=True,
                    help='left row-ordered matrix')
parser.add_argument('-r', '--right', type=int, nargs='+', required=True,
                    help='right row-ordered matrix')
args = parser.parse_args()

def multiply_matrix(left_array, right_array):
    left_n = get_matrix_size(left_array)
    right_n = get_matrix_size(right_array)

    if left_n != right_n:
        raise ValueError('you should provide two matrix with the same size')

    n = left_n
    result = [None] * len(left_array)

    # Zij = SUM[k=1 till k = n] Xik * Ykj
    for row in xrange(0, n):
        for column in xrange(0, n):
            cell = 0
            for k in xrange(0, n):
                cell += left_array[row * n + k] * right_array[k * n + column]
            result[row * n + column] = cell

    return result

def get_matrix_size(arr):
    sqrt_len = math.sqrt(len(arr))

    if int(sqrt_len) == sqrt_len:
        return int(sqrt_len)

    raise ValueError('you should provide matrix with quadratic length')


def main():
    print multiply_matrix(args.left, args.right)

if __name__ == '__main__':
    main()
