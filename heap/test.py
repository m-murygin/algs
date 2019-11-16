#!/usr/bin/python3


import heapq
import random
from heap import Heap


def main():
    arr = []
    heap = Heap()

    random.seed(1)
    for i in range(10):
        num = random.randrange(100)
        arr.append(num)
        heap.push(num)

    heapq.heapify(arr)
    print(arr)
    print(heap)

    for i in range(5):
        index = len(arr) // 2

        val = arr[index]
        heap.delete(val)

        del arr[index]
        heapq.heapify(arr)

    print(arr)
    print(heap)


if __name__ == "__main__":
    main()
