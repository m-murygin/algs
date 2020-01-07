#!/usr/bin/python3


def count_the_paths(grid):
    total_rows = len(grid)
    total_cols = len(grid[0])

    for i in range(total_rows - 1, -1, -1):
        for j in range(total_cols):
            if i == total_rows - 1 and j == 0:
                continue

            if grid[i][j] == 0:
                continue

            bottom_paths = grid[i + 1][j] if i + 1 < total_rows else 0
            left_paths = grid[i][j - 1] if j - 1 >= 0 else 0

            grid[i][j] = bottom_paths + left_paths

    print(grid)

    return grid[0][total_cols-1]


def main():
    n = int(input())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().split())))

    print(grid)

    paths = count_the_paths(grid)
    print(paths)


if __name__ == "__main__":
    main()
