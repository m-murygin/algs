#!/usr/bin/python3

def binary_search(a, key):
  if len(a) == 0:
    return -1

  start = 0
  end = len(a)
  while end - start > 1:
    mid = (start + end) // 2

    print(start, end, mid)
    if key < a[mid]:
      end = mid
    elif key > a[mid]:
      start = mid
    else:
      return mid

  if a[start] == key:
    return start

  return -1


def main():
  key = int(input())
  arr = list(map(int, input().split()))
  res = binary_search(arr, key)

  print(res)


if __name__ == "__main__":
  main()
