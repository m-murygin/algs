class ValuesDict:
    def __init__(self):
        self.values = {}

    def push(self, index, value):
        if value in self.values:
            self.values[value].append(index)
        else:
            self.values[value] = [index]

    def delete(self, index, value):
        self.values[value].remove(index)

    def swap(self, from_index, from_value, to_index, to_value):
        self.values[from_value].remove(from_index)
        self.values[from_value].append(to_index)
        self.values[to_value].remove(to_index)
        self.values[to_value].append(from_index)

    def get_index_by_value(self, value):
        return self.values[value][0]


class Heap:
    def __init__(self):
        self.arr = []
        self.values = ValuesDict()

    def push(self, n):
        index = len(self.arr)

        self.arr.append(n)
        self.values.push(index, n)

        self.__sift_up__(index)

    def pop(self):
        index = len(self.arr) - 1

        self.__swap__(0, index)

        val = self.arr.pop()
        self.values.delete(index, val)

        self.__sift_down__(0)
        return val

    def peek(self):
        return self.arr[0]

    def delete(self, value):
        index_from = self.values.get_index_by_value(value)
        index_to = len(self.arr) - 1

        self.__swap__(index_from, index_to)
        val = self.arr.pop()
        self.values.delete(index_to, val)

        self.__sift_up__(index_from)
        self.__sift_down__(index_from)

    def __str__(self):
        return f"[{', '.join(map(str, self.arr))}]"

    def __get_parent_index__(self, i):
        if i == 0:
            return -1

        return i // 2 - (1 if i % 2 == 0 else 0)

    def __get_left_child__(self, i):
        child = 2*i + 1

        return child if child < len(self.arr) else -1

    def __get_right_child__(self, i):
        child = 2*i + 2

        return child if child < len(self.arr) else -1

    def __swap__(self, i, j):
        self.values.swap(i, self.arr[i], j, self.arr[j])

        val = self.arr[i]
        self.arr[i] = self.arr[j]
        self.arr[j] = val

    def __sift_up__(self, i):
        parent = self.__get_parent_index__(i)

        if parent == -1:
            return

        if self.arr[i] < self.arr[parent]:
            self.__swap__(i, parent)
            self.__sift_up__(parent)

    def __sift_down__(self, i):
        left_child = self.__get_left_child__(i)
        right_child = self.__get_right_child__(i)

        if left_child == -1:
            return

        if right_child == -1:
            min_child = left_child
        else:
            min_child = left_child \
                if self.arr[left_child] <= self.arr[right_child] \
                else right_child

        if self.arr[i] > self.arr[min_child]:
            self.__swap__(i, min_child)
            self.__sift_down__(min_child)
