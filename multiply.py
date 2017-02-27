#!/usr/bin/env python

import argparse
import math


parser = argparse.ArgumentParser(description='Multiplies two objects.')
parser.add_argument('first', type=int,
                    help='an integer for the multyplication')
parser.add_argument('second', type=int,
                    help='an integer for the multyplication')
args = parser.parse_args()


def main():
    result = multiply(args.first, args.second)
    print 'result %s' % result


# Karatsuba Multiplication
# x * y = (10^n)ac + (10^0.5n) * (ad + bc) + bd
# where:
# ad + bc = (a + b) * (c + d) - ac - bd
# example:
# 1234 * 5678
# a = 12 b = 34 c = 56 d = 78
def multiply(first, second):
    first_str = str(first)
    second_str = str(second)
    n = max(len(first_str), len(second_str))

    if n == 1:
        return first * second

    half_n = n / 2 + n % 2

    a = get_int_partitial(first_str[:-half_n])
    b = get_int_partitial(first_str[-half_n:])
    c = get_int_partitial(second_str[:-half_n])
    d = get_int_partitial(second_str[-half_n:])

    ac = multiply(a, c)
    bd = multiply(b, d)
    ad_plus_bc = multiply(a + b, c + d) - ac - bd

    return pow(10, 2 * half_n) * ac + pow(10, half_n) * ad_plus_bc + bd


def get_int_partitial(str_partitial):
    return int(str_partitial) if len(str_partitial) > 0 else 0


if __name__ == '__main__':
    main()
