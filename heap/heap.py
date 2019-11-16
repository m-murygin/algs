class Heap:
    def __init__(self):
        self.arr = []

    def pop(self):
        self.__swap__(0, len(self.arr) - 1)
        val = self.arr.pop()
        self.__move_down__(0)
        return val

    def push(self, n):
        self.arr.append(n)
        self.__move_up__(len(self.arr) - 1)

    def peek(self):
        return self.arr[0]

    def delete(self, value):
        pass

    def __str__(self):
        return f"[{', '.join(map(str, self.arr))}]"

    def __get_parent_index__(self, i):
        return i // 2 - (1 if i % 2 == 0 else 0)

    def __get_left_child__(self, i):
        child = 2*i + 1

        return child if child < len(self.arr) else -1

    def __get_right_child__(self, i):
        child = 2*i + 2

        return child if child < len(self.arr) else -1

    def __swap__(self, i, j):
        val = self.arr[i]
        self.arr[i] = self.arr[j]
        self.arr[j] = val

    def __move_up__(self, i):
        parent = self.__get_parent_index__(i)

        if parent == -1:
            return

        if self.arr[i] < self.arr[parent]:
            self.__swap__(i, parent)
            self.__move_up__(parent)

    def __move_down__(self, i):
        print("Before move down", self)
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
            self.__move_down__(min_child)

        print("After move down", self)
