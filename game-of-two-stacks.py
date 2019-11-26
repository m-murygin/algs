#!/usr/bin/python3

from collections import deque


def get_els_to_fit(x, stack):
    index = -1
    # iterate through stack
    while len(stack) >= (-1) * index:
        if x - stack[index] >= 0:
            x -= stack[index]
            index -= 1
        else:
            break

    return -1 * (index + 1)


def two_stacks(x, a, b):
    print(f"two_stacks for x = {x}")
    a_stack = deque()
    for el in a:
        a_stack.appendleft(el)
    print(a_stack)

    b_stack = deque()
    for el in b:
        b_stack.appendleft(el)
    print(b_stack)

    cur_sum = 0
    a_elements_in_result = 0
    result = deque()
    while len(a_stack) > 0:
        el = a_stack[-1]

        if cur_sum + el > x:
            break
        else:
            cur_sum += el
            result.append(a_stack.pop())
            a_elements_in_result += 1

    while len(b_stack) > 0:
        el = b_stack[-1]

        if cur_sum + el > x:
            break
        else:
            cur_sum += el
            result.appendleft(b_stack.pop())

    while len(b_stack) > 0 and a_elements_in_result > 0:
        print(f"considering replace: {result}, {b_stack}")
        els_to_fit = get_els_to_fit(x - cur_sum + result[-1], b_stack)
        print(f"els_to_fit: {els_to_fit}")

        if els_to_fit > 1 or (els_to_fit == 1 and b_stack[-1] < result[-1]):
            a_elements_in_result -= 1
            cur_sum -= result.pop()
            while els_to_fit > 0:
                els_to_fit -= 1
                to_add = b_stack.pop()
                cur_sum += to_add
                result.appendleft(to_add)
            print(f"after replace: {result}, {b_stack}")
        else:
            break

    print(f"result: {result}")
    return result


def main():
    real_answers = []
    with open("/tmp/two-s/output") as f:
        for line in f:
            real_answers.append(int(line))

    q = int(input())
    results = []
    for n in range(q):
        print("--------------------")
        a_len, b_len, x = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        results.append(two_stacks(x, a, b))

        if real_answers[n] != len(results[n]):
            print(f"ERROR: {results[n]} should be {real_answers[n]}")
            print(a)
            print(b)
            print(x)
            print(results[n])
            break


if __name__ == "__main__":
    main()
