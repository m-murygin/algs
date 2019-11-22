#!/usr/bin/python3

from collections import Counter


def print_dict_in_order(d):
    print(", ".join(map(lambda x: f"{x}:{d[x]}", sorted(d.keys()))))


class BruteForce:
    def __init__(self):
        self.freq = {}
        self.answer = []

    def process_query(self, query):
        command, val = query
        if command == 1:
            self.freq[val] = self.freq.get(val, 0) + 1
        elif command == 2:
            if val in self.freq:
                self.freq[val] -= 1
                if self.freq[val] == 0:
                    del self.freq[val]
        else:
            self.answer.append(1 if val in self.freq.values() else 0)


class TwoHashTables:
    def __init__(self):
        self.freq = {}
        self.rep = {}
        self.answer = []

    def process_query(self, query):
        command, val = query
        if command == 1:
            if val in self.freq:
                prev_freq = self.freq[val]
                new_freq = self.freq[val] + 1
                self.freq[val] = new_freq
                if self.rep[prev_freq] == 1:
                    del self.rep[prev_freq]
                else:
                    self.rep[prev_freq] -= 1
                self.rep[new_freq] = self.rep.get(new_freq, 0) + 1
            else:
                new_freq = 1
                self.freq[val] = new_freq
                self.rep[new_freq] = self.rep.get(new_freq, 0) + 1
        elif command == 2:
            if val in self.freq:
                prev_freq = self.freq[val]
                new_freq = self.freq[val] - 1
                self.rep[prev_freq] -= 1

                if new_freq == 0:
                    del self.freq[val]
                else:
                    self.freq[val] = new_freq
                    self.rep[new_freq] = self.rep.get(new_freq, 0) + 1
        elif command == 3:
            res = 1 if val in self.rep else 0
            self.answer.append(res)
        else:
            raise Exception("Unknown command")


def freqQuery(queries, brute_result):
    freq = {}
    rep = {}
    answer = []
    for query in queries:
        print(f"After: {query}")
        print_dict_in_order(freq)
        print_dict_in_order(rep)
        y = Counter(freq.values())
        print_dict_in_order(y)
        x = rep
        shared_items = {k: x[k] for k in x if k in y and x[k] == y[k]}
        if len(shared_items) != len(x):
            print("FOUND!!!!!")
            print(y)
        print("\n")

    return answer


if __name__ == '__main__':
    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    two_hash = TwoHashTables()
    brute_force = BruteForce()

    for q in queries:
        print(f"BEFORE: {q}")
        print_dict_in_order(two_hash.freq)
        print_dict_in_order(brute_force.freq)
        print_dict_in_order(two_hash.rep)
        two_hash.process_query(q)
        brute_force.process_query(q)
        print("AFTER")
        print_dict_in_order(two_hash.freq)
        print_dict_in_order(brute_force.freq)
        print_dict_in_order(two_hash.rep)
        print("\n")

    print(two_hash.answer)
    print(brute_force.answer)
