#!/usr/bin/python3


def get_window_min(arr, from_index, to_index, prev_windows):
    print(f"get_window_min for [{from_index}, {to_index}]")
    if from_index == to_index:
        return arr[from_index]

    return min(prev_windows[from_index], arr[to_index])


def riddle(arr):
    riddles = [None] * len(arr)

    prev_windows = None
    for w_size in range(1, len(arr) + 1):
        print(f"calculate for w_size = {w_size}")
        windows = []
        for from_idx in range(0, len(arr) - w_size + 1):
            to_index = from_idx + w_size - 1
            windows.append(
                get_window_min(arr, from_idx, to_index, prev_windows)
            )
            print(f"windows {windows}")

        riddles[w_size - 1] = max(windows)
        prev_windows = windows
        print(f"riddle: {max(windows)}")

    return riddles


def main():
    arr = list(map(int, input().rstrip().split()))

    res = riddle(arr)

    print(res)


if __name__ == "__main__":
    main()
