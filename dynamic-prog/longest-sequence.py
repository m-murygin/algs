#!/usr/bin/python3


def longest_increasing(seq):
    res = [None] * len(seq)
    for i in range(len(seq)):
        longest_index = -1
        longest_len = 0
        for j in range(i):
            if seq[j] < seq[i]:
                if longest_len < len(res[j]) + 1:
                    longest_len = len(res[j]) + 1
                    longest_index = j

        if longest_index == -1:
            res[i] = []
        else:
            res[i] = res[longest_index].copy()

        res[i].append(seq[i])

    max_seq = []
    for seq_res in res:
        if len(seq_res) > len(max_seq):
            max_seq = seq_res

    return max_seq


def main():
    seq = list(map(int, input().split()))

    longest = longest_increasing(seq)
    print(longest)


if __name__ == "__main__":
    main()
