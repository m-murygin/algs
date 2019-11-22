#!/usr/bin/python3


def is_abbreviation(str, search):
    for i in range(search):
        return "YES"


def main():
    src = input()
    search = input()

    print(is_abbreviation(src, search))


if __name__ == "__main__":
    main()
