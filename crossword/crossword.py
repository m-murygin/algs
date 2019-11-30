#!/usr/bin/python3

from collections import deque


class CrossWord:
    EMPTY_CELL = '-'
    BLACK_CELL = '+'

    def __init__(self, cells, words):
        self.cells = cells
        self.words = set(words)

    def fill(self):
        empty_cell = self.get_empty_cell()

        if not empty_cell:
            return True

        gap = Gap(self.cells, empty_cell)

        while True:
            word = self.get_match_word(gap)

            if not word:
                return False

            self.fill_word(gap, word)

            if self.fill():
                return True
            else:
                gap.not_matched_words.add(word)
                self.clear_word(gap, word)

    def get_empty_cell(self):
        for row in range(len(self.cells)):
            for column in range(len(self.cells[row])):
                if self.cells[row][column] == CrossWord.EMPTY_CELL:
                    return row, column

    def get_match_word(self, gap):
        for word in self.words:
            if gap.match(self.cells, word):
                return word

    def fill_word(self, gap, word):
        for i in range(len(gap.cells)):
            row, col = gap.cells[i]

            self.cells[row][col] = word[i]

        self.words.remove(word)

    def clear_word(self, gap, word):
        for row, col in gap.cells:
            self.cells[row][col] = CrossWord.EMPTY_CELL

        self.words.add(word)

    def print(self):
        print("Crossword")
        print(f"words: {self.words}")
        for row in range(len(self.cells)):
            for col in range(len(self.cells[row])):
                print(self.cells[row][col], end='')
            print()


class Gap:
    def __init__(self, all_cells, first_empty):
        self.not_matched_words = set()
        self.first_empty = first_empty
        self._fill_cells(all_cells)

    def _fill_cells(self, all_cells):
        if self._is_horizontal(all_cells):
            cells = self._get_horizontal_cells(all_cells)
        else:
            cells = self._get_vertical_cells(all_cells)

        self.cells = cells

    def _is_horizontal(self, all_cells):
        row, col = self.first_empty

        # check left cell
        if col > 0 and all_cells[row][col - 1] != CrossWord.BLACK_CELL:
            return True

        # check right cell
        if col + 1 < len(all_cells[row]) \
                and all_cells[row][col + 1] != CrossWord.BLACK_CELL:
            return True

        return False

    def _get_horizontal_cells(self, all_cells):
        row, col = self.first_empty
        cells = deque()
        cells.append((row, col))

        cur_col = col - 1
        while cur_col >= 0:
            if all_cells[row][cur_col] != CrossWord.BLACK_CELL:
                cells.appendleft((row, cur_col))
                cur_col -= 1
            else:
                break

        cur_col = col + 1
        while cur_col < len(all_cells[row]):
            if all_cells[row][cur_col] != CrossWord.BLACK_CELL:
                cells.append((row, cur_col))
                cur_col += 1
            else:
                break

        return list(cells)

    def _get_vertical_cells(self, all_cells):
        row, col = self.first_empty
        cells = deque()
        cells.append((row, col))

        cur_row = row - 1
        while cur_row >= 0:
            if all_cells[cur_row][col] != CrossWord.BLACK_CELL:
                cells.appendleft((cur_row, col))
                cur_row -= 1
            else:
                break

        cur_row = row + 1
        while cur_row < len(all_cells):
            if all_cells[cur_row][col] != CrossWord.BLACK_CELL:
                cells.append((cur_row, col))
                cur_row += 1
            else:
                break

        return list(cells)

    def match(self, cells, word):
        if word in self.not_matched_words:
            return False

        if len(word) != len(self.cells):
            return False

        for i in range(len(self.cells)):
            row, col = self.cells[i]

            if cells[row][col] != CrossWord.EMPTY_CELL and \
                    word[i] != cells[row][col]:
                return False

        return True


def crosswordPuzzle(inp_cells, words):
    words = words.split(';')
    cells = [[c for c in row] for row in inp_cells]

    crossword = CrossWord(cells, words)
    crossword.fill()

    return [''.join(row) for row in crossword.cells]


def main():
    crossword = []

    for _ in range(10):
        crossword_item = input()
        crossword.append(crossword_item)

    words = input()

    result = crosswordPuzzle(crossword, words)

    print('\n'.join(result))


if __name__ == '__main__':
    main()
