#!/usr/bin/python3

#################################
# 3  2  1  1  1  4  3  2  2  1  0

# 1  0 -1 -1 -1  0 -1 -2 -2 -3 -4
# 6  5  4  4  4  5  4  3  3  2  1

# 3  2  1  1  1  3  2  1  3  2  1

#################################

MIN_CANDIES = 1


def backtrack(students, res, index):
    if res[index] >= MIN_CANDIES:
        return

    res[index] = MIN_CANDIES

    while index > 0:
        if students[index - 1] > students[index]:
            res[index - 1] = max(res[index - 1], res[index] + 1)
            index -= 1
        else:
            break


def calc_student_candies(students, results, index):
    if index == 0:
        results[index] = MIN_CANDIES
    elif students[index] > students[index - 1]:
        backtrack(students, results, index - 1)
        results[index] = results[index - 1] + 1
    elif students[index] == students[index - 1]:
        backtrack(students, results, index - 1)
        results[index] = MIN_CANDIES
    else:
        results[index] = min(MIN_CANDIES, results[index - 1] - 1)


def candies(n, students):
    results = [0] * n

    for i in range(1, len(students)):
        calc_student_candies(students, results, i)

    backtrack(students, results, n - 1)

    print(students)
    print(results)
    return sum(results)


def main():
    n = int(input())
    students = [0] * n
    for i in range(n):
        students[i] = int(input())

    total = candies(n, students)
    print(total)


if __name__ == "__main__":
    main()
