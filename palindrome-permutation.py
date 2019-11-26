#!/usr/bin/python3

from collections import Counter


def has_palindrome_permutation(string):
    chars_count = Counter(string)
    allow_not_even = len(string) % 2 == 1

    for char_count in chars_count.values():
        if char_count % 2 == 1:
            if allow_not_even:
                allow_not_even = False
            else:
                return False

    return True


def main():
    while True:
        in_str = input()
        print(f"Result: {has_palindrome_permutation(in_str)}")


if __name__ == "__main__":
    main()
