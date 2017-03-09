#!/usr/bin/python

# X * Y = ?
# X = (A B)   Y = (E F)
#     (C D)       (G H)
# X * Y = (AE+BG AF+BH) = (P5-P4-P2+P6     P1+P2   )
#         (CE+DG CF+DH)   (   P3+P4     P1+P5-P3-P7)
# where:
# P1 = A * (F - H)
# P2 = (A + B) * H
# P3 = (C + D) * E
# P4 = D * (G - E)
# P5 = (A + D) * (E + H)
# P6 = (B - D) * (G + H)
# P7 = (A - C) * (E + F)


import argparse
import math

parser = argparse.ArgumentParser(
    description='Multiplies two matrixes with strassen\'s algorithm')
parser.add_argument('-l', '--left', type=int, nargs='+', required=True,
                    help='left row-ordered matrix')
parser.add_argument('-r', '--right', type=int, nargs='+', required=True,
                    help='right row-ordered matrix')
args = parser.parse_args()

def multiply_matrix(left_array, right_array):
    return 'Not implemented'


def main():
    print multiply_matrix(args.left, args.right)

if __name__ == '__main__':
    main()
